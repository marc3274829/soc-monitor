from collections import defaultdict
from datetime import datetime, timedelta
from config import Config

failed_logins = defaultdict(list)

TIME_WINDOW = timedelta(minutes=2)


def detect(parsed_log):
    event=parsed_log["event"]
    ip = parsed_log["ip"]
    timestamp = datetime.strptime(parsed_log["timestamp"], "%Y-%m-%d %H:%M:%S")

    if event == "LOGIN_FAILED":
        failed_logins[ip].append(timestamp)

        # keep only recent attempts
        failed_logins[ip] = [
            t for t in failed_logins[ip]
            if timestamp - t <= TIME_WINDOW
        ]

        if len(failed_logins[ip]) >= Config.FAILED_LOGIN_THRESHOLD:
            return {
                "type": "BRUTE_FORCE",
                "ip": ip,
                "severity": "HIGH",
                "message": f"Too many failed logins from {ip}"
            }
    
    return None
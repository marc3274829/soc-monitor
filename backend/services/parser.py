import re

log_pattern = r"^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<event>\w+) user=(?P<user>\w+) ip=(?P<ip>\d+\.\d+\.\d+\.\d+)$"

def parse_log_entry(log_line):
    match = re.match(log_pattern, log_line)
    if match:
        timestamp = match.group("timestamp")
        event = match.group("event")
        user = match.group("user")
        ip = match.group("ip")

        return {
            "timestamp": timestamp,
            "event": event,
            "user": user,
            "ip": ip
        }

    return None


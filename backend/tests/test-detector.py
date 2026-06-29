from backend.services.detector import detect

logs = [
    {"timestamp": "2026-06-29 12:00:01", "event": "LOGIN_FAILED", "user": "alice", "ip": "1.1.1.1"},
    {"timestamp": "2026-06-29 12:00:10", "event": "LOGIN_FAILED", "user": "alice", "ip": "1.1.1.1"},
    {"timestamp": "2026-06-29 12:00:20", "event": "LOGIN_FAILED", "user": "alice", "ip": "1.1.1.1"},
    {"timestamp": "2026-06-29 12:00:30", "event": "LOGIN_FAILED", "user": "alice", "ip": "1.1.1.1"},
    {"timestamp": "2026-06-29 12:00:40", "event": "LOGIN_FAILED", "user": "alice", "ip": "1.1.1.1"},
]

for log in logs:
    alert = detect(log)
    print("ALERT:", alert)
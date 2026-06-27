# Security Monitoring Dashboard
## Architecture

### Overview

The Security Monitoring Dashboard is a Python-based web application designed to monitor, analyse and visualise security events from various log sources.

The system is divided into independent components responsible for log collection, parsing, detection, storage and presentation. This modular architecture allows individual components to be expanded or replaced without affecting the remainder of the application

## High Level Architecture

        Log Files
            |
            ▼
        Log Collection
            |
            ▼
        Log Parser Module
            |
            ▼
        Detection Engine
            |
            ▼
        Event Database
            |
   ┌────────┴────────┐
Dashboard/API       Alert Engine


## Components


### Backend

Responsible for:

- Reading security logs
- Parsing log entries
- Detecting suspicious activity
- Storing processed events
- Providing API endpoints


### Frontend

Responsible for:

- Displaying security events
- Charts
- Alerts
- Dashboard statistics


### Log Sources

Intially the application will support:

- Windows Event Logs (sample data)
- Linux Syslog
- Authentication logs

Future support may include:

- Web server logs
- Firewall logs
- IDS alerts


### Detection Engine

The detection engine analyses parsed logs for suspicious behaviour.

Examples include:

- Failed login threshold exceeded
- Brute-force attacks
- Privilege escalation
- Suspicious IP activity

---

### Data Storage

Initially:

- SQLite

Possible future expansion:

- PostgreSQL
- Elasticsearch

---

### Technologies

| Component | Technology |
|------------|------------|
| Backend | Python |
| Frontend | Flask + HTML/CSS |
| Database | SQLite |
| Visualisation | Chart.js |
| Version Control | Git |
| Repository | GitHub |

---

## Future Enhancements

- User authentication
- Role Based Access Control
- Email alerts
- Live monitoring
- Docker deployment
- SIEM integrations
- Threat intelligence feeds
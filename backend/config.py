import os

class Config:
    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = True

    # Database
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///events.db")


    # Security
    LOG_PATH = os.getenv("LOG_PATH", "data/auth.log")

    # Detection Thresholds
    FAILED_LOGIN_THRESHOLD = int(os.getenv("FAILED_LOGIN_THRESHOLD", 3))
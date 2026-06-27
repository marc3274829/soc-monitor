import os

class Config:
    # Flask Settings
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    DEBUG = True

    # Database
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///events.db")
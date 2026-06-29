from flask import Blueprint
from services.log_reader import read_logs

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/logs")
def get_logs():
        
        lines = read_logs("data/auth.log")


        return {
                "logs": lines
        }
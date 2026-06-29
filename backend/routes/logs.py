from flask import Blueprint

logs_bp = Blueprint("logs", __name__)

@logs_bp.route("/logs")
def get_health():
        return {
                "message": "Log API"
        }
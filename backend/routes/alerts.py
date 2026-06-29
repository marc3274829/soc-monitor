from flask import Blueprint

alerts_bp = Blueprint("alerts", __name__)

@alerts_bp.route("/alerts")
def get_alerts():
        return {
                "alerts": []
        }
from flask import Blueprint

events_bp = Blueprint("events", __name__)

@events_bp.route("/events")
def get_events():
        return {
                "events": []
        }
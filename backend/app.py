from flask import Flask
from config import Config
from routes.health import health_bp
from routes.events import events_bp
from routes.logs import logs_bp

app = Flask(__name__)

# Load application configuration
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(health_bp)
app.register_blueprint(events_bp)
app.register_blueprint(logs_bp)


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
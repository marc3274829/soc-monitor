from flask import Flask
from config import Config
from routes.health import health_bp

app = Flask(__name__)

# Load application configuration
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
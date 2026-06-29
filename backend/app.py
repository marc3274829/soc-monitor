from flask import Flask
from config import Config

app = Flask(__name__)

# Load application configuration
app.config.from_object(Config)

# simple test route
@app.route("/")
def home():
    return {
        "message": "Backend is running"
    }

if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"])
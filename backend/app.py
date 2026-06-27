from flask import Flask

app = Flask(__name__)

# simple test route
@app.route("/")
def home():
    return {"message": "Backend is running"}

if __name__ == "__main__":
    app.run(debug=True)
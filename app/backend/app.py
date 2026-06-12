from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Hello from Backend",
        "version": "v1",
        "service": "backend"
    })

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

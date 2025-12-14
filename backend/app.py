from flask import Flask, jsonify, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Cloud Evolution Backend is running"

@app.route("/api/timesteps")
def timesteps():
    return jsonify({"timesteps": [0, 1, 2]})

@app.route("/api/image/<int:t>")
def image(t):
    path = f"cache/t{t}.png"
    if os.path.exists(path):
        return send_file(path)
    return "Image not found", 404

@app.route("/api/graph")
def graph():
    return jsonify({
        "nodes": [],
        "edges": []
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, request, jsonify
import os
app = Flask(__name__)

DB_PASSWORD = os.getenv("DB_PASSWORD")

@app.route("/pay", methods=["POST"])
def pay():
    return jsonify({"status": "payment successful"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

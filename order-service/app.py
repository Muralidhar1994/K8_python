from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# Read configuration from environment variables
PAYMENT_URL = os.getenv("PAYMENT_URL")
LOG_LEVEL = os.getenv("LOG_LEVEL")

@app.route("/order")
def order():

    response = requests.post("http://payment-service/pay")

    return jsonify({
        "order": "created",
        "payment": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

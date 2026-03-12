from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/order")
def order():

    response = requests.post("http://payment-service/pay")

    return jsonify({
        "order": "created",
        "payment": response.json()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

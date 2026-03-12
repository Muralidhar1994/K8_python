from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pay", methods=["POST"])
def pay():
    return jsonify({"status": "payment successful"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

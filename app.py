from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "Mhanzsecure2026asdasdasdasdasdasd"
ENDPOINT_URL = "https://ebayserver-i0dn.onrender.com/ebay-webhook"

@app.route("/")
def home():
    return "Online"

@app.route("/ebay-webhook", methods=["GET", "POST"])
def ebay_webhook():

    if request.method == "GET":
        challenge_code = request.args.get("challenge_code", "")

        data = challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL
        challenge_response = hashlib.sha256(data.encode()).hexdigest()

        return jsonify({
            "challengeResponse": challenge_response
        })

    return "", 200

if __name__ == "__main__":
    app.run()

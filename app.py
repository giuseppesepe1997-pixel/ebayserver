from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Online"

@app.route("/ebay-webhook", methods=["GET","POST"])
def ebay():
    return "OK"

if __name__ == "__main__":
    app.run()
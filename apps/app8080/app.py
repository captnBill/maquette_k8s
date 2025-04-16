from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from app 8080!"

app.run(host="0.0.0.0", port=8080)

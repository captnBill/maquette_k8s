from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from app 9090!"

app.run(host="0.0.0.0", port=9090)

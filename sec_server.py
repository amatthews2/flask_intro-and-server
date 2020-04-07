from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Index!"


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/num")
def members():
    return 5


if __name__ == "__main__":
    app.run(debug=True)

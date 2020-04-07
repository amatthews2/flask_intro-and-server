from flask import Flask

app = Flask(__name__)


@app.route("/api/new_patient", methods=["GET"])
def patient_info():
    return "r!"


@app.route("/api/heart_rate")
def hello():
    return "Hello World!"


@app.route("/num")
def members():
    return 5


if __name__ == "__main__":
    app.run(debug=True)
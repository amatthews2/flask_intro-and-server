from flask import Flask, jsonify, request

app = Flask(__name__)
patient_database = []


@app.route("/api/new_patient", methods=["POST"])
def patient_info():
    patient_to_add = request.get_json()
    patient_database.append(patient_to_add)
    return "Patient {} added".format(patient_to_add)


@app.route("/api/get_patient", methods=["GET"])
def patient():
    return patient_database


@app.route("/api/heart_rate")
def hello():
    return "Hello World!"


@app.route("/")
def home():
    return "You need to put the API"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, jsonify, request

app = Flask(__name__)
patient_info = []
patient_data = []
pat = {}
pat2 = {}


@app.route("/api/new_patient", methods=["POST"])
def patient_info():
    patient_to_add = request.get_json()
    pat["patient_id"] = integer_check(patient_to_add["patient_id"])
    pat["att_email"] = patient_to_add["attending_email"]
    pat["patient_age"] = integer_check(patient_to_add["patient_age"])
    patient_data.append(pat)
    logging.info()
    return "Patient {} added".format(patient_to_add)


def integer_check(pat_ID):
    if isinstance(pat_ID, int):
        int(pat_ID)
    elif pat_ID.isdigit():
        int(pat_ID)
    else:
        error_return()
        breakpoint()
    return pat_ID

def error_return():
    return "There is an error in the patient information given"


@app.route("/api/heart_rate", methods=["POST"])
def patient_data():
    patient_data = request.get_json()
    pat2["patient_id"] = integer_check(patient_data["patient_id"])
    pat2["heart_rate"] = integer_check(patient_data["heart_rate"])
    patient_data.append(pat2)
    return "Patient {} added".format(pat2)


def integer_check(pat_ID):
    if isinstance(pat_ID, int):
        int(pat_ID)
    elif pat_ID.isdigit():
        int(pat_ID)
    else:
        error_return()
        breakpoint()


def error_return():
    return "There is an error in the patient information given"


@app.route("/api/get_heart_rate", methods=["GET"])
def patient():
    return jsonify(patient_data)


@app.route("/")
def home():
    return "You need to put the API"


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, request, jsonify
import datetime
import logging

logging.basicConfig(filename="server_log.txt", level=logging.DEBUG)

db = []

app = Flask(__name__)


@app.route("/api/new_patient/", methods=["POST"])
def add_patient():
    new_patient = request.json()
    expected_keys = ("patient_id", "attending_email", "patient_age")
    expected_type = (int, str, int)
    pat, valid = verify_info(new_patient, expected_keys, expected_type)
    if valid is not True:
        return pat, 400
    pat["heart_rate"] = []
    pat["status"] = []
    pat["timestamp"] = []
    db.append(pat)
    logging.info("Patient {} has been added".format(pat["patient_ID"]))
    return "Patient Added", True


def verify_info(in_dict, expected_keys, expected_type):
    for i, key in enumerate(expected_keys):
        if key not in in_dict.keys():
            return "{} key not found".format(key), 404
        if type(in_dict[key]) is not expected_type[i]:
            if in_dict[key].isdigit() is False:
                return "{} is wrong type".format(key), 400
            else:
                in_dict[key] = int(in_dict[key])
    return in_dict, True


def error(status_code, text, err_type):
    error_output = {
        "status_code": status_code,
        "reason": text,
        "error_type": err_type
    }
    return jsonify(error_output)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)

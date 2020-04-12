import requests

# server_name = "vcm-14488.vm.duke.edu:5004"
server_name = "https:127.0.0.1:5000"

new_patient = {"patient_id": "100000000",
               "attending_email": "r_user_id@yourdomain.com",
               "patient_age": 50}
r = requests.post(server_name,
                  json=new_patient)
print(r.status_code)
print(r.text)

patient_data = {"patient_id": "1", "heart_rate": "100"}
r = requests.post(server_name,
                  json=patient_data)
print(r.status_code)
print(r.text)


def add_some_patients():
    new_p = {"patient_id": "1", "heart_rate": "100"}
    r = requests.post(server_name,
                      json=patient_data)
    if r.status_code != 200:
        print("Error: {} - {}".format(r.status_code, r.text))
    else:
        print("success {}".format(r.text))


if __name__ == '__main__':
    add_some_patients()

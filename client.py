import requests

new_patient = {"patient_ID": "1", "attending_email": "r_user_id@yourdomain.com",
             "patient_age": 50}
r = requests.post("http://127.0.0.1:5000/api/new_patient", json=new_patient)
print(r.status_code)
print(r.text)

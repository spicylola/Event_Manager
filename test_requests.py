import requests
import datetime
import json


# Test Create Events
API_ENDPOINT = "http://127.0.0.1:5000/events"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {"events":{"name":"Spicy Lola Pepper contest", "created_by" : 6, "status": "pending", "start_time": str(datetime.datetime.utcnow()), "end_time": str(datetime.datetime.utcnow()), "description": " Woot woot", "location": "Atlanta, GA"}}
r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers)
print(r.text, r.status_code)

# Test Put Events 
API_ENDPOINT = "http://127.0.0.1:5000/events"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {"events":{"name":"Spicy Lola Pepper contest", "created_by" : 6, "status": "approved"}, "id":5}
r = requests.put(url = API_ENDPOINT, data = json.dumps(data), headers=headers)
print(r.text, r.status_code)


# Test GET EVENTS BY ADMIN
payload = {"pending_admin": 1}
r = requests.get(url = API_ENDPOINT+"?pending_admin=1")
print(r.text, r.status_code)

# Test GET EVENTS BY USER
payload = {'created_by': 6}
r = requests.get(url = API_ENDPOINT+"?created_by=7")
print(r.text, r.status_code)

#Test GET ALL EVENTS
payload = {"show_all": 1}
r = requests.get(url = API_ENDPOINT+"?show_all=1")
print(r.text, r.status_code)

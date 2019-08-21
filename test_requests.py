import requests
import datetime
import json


# Test Create Events
API_ENDPOINT = "http://127.0.0.1:5000/events"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {"events":{"name":"Spicy Lola Pepper contest", "created_by" : 7, "status": "pending", "start_time": str(datetime.datetime.utcnow()), "end_time": str(datetime.datetime.utcnow()), "description": " Woot woot", "location": "Atlanta, GA"}}
r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers=headers)
print(r.text, r.status_code)

# Test Put Events 
API_ENDPOINT = "http://127.0.0.1:5000/events"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = {"events":{"name":"Spicy Lola Pepper contest", "created_by" : 7, "status": "approved"}, "id":7}
r = requests.put(url = API_ENDPOINT, data = json.dumps(data), headers=headers)
print(r.text, r.status_code)


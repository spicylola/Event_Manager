import requests
import datetime



# Test Create Events
API_ENDPOINT = "http://localhost:5000/events"
data = {"name":"Spicy Lola Pepper contest", "created_by" : 7, "event_status": "pending", "start_time": datetime.datetime.utcnow(), "end_time": datetime.datetime.utcnow(), "description": 
       {"details":" Woot woot"}, "location": "Atlanta, GA"}
r = requests.post(url = API_ENDPOINT, data = data)




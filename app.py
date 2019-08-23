import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#cors = CORS(app)
db = SQLAlchemy(app)
from models import *


CORS(app, support_credentials=True)





@app.route('/')
def hello():
    return "Hello World!"

@app.route("/events", methods=['GET', 'PUT', 'POST'])
@cross_origin(supports_credentials=True)
def cru_events():
    """
    Retrieve, update or create admin/regular users.
    """
    if request.method == 'POST':
       raw_event_data = request.get_json()
       event_data = raw_event_data.get("events")
       print(event_data)
       new_event = Events(**event_data)
       db.session.add(new_event)
       db.session.commit()
       return str(event_data)

    if request.method == 'PUT':
       raw_event_data = request.get_json()
       event_id = raw_event_data.pop("id")
       print(event_id)
       event_info = db.session.query(Events).filter(Events.id ==event_id)
       print(event_info)
       event_info.update(raw_event_data['events'])       
       db.session.commit()
       return str(raw_event_data)


    # TODO: Filter by USER ID
    if request.method == 'GET':
       params = request.args
             
       if "show_all" in params:
           event_info = db.session.query(Events).filter(Events.status == "approved").all()
           print(str(event_info))
           return str(event_info)
       if "pending_admin" in params:
           event_info = db.session.query(Events).filter(Events.status == "pending").all()
           print(str(event_info))
           return str(event_info)
       if "created_by" in params and params.get('created_by') is not None:
           event_info = db.session.query(Events).filter(Events.id == params.get('created_by')).all()
           print(str(event_info))
           return str(event_info)
       return "Error Processing Dict"
 

if __name__ == '__main__':
    app.run()

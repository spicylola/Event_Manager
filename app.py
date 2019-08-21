import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import *

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/events", methods=['GET', 'PUT', 'POST'])
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
    #if request.method == 'GET':
    #if key not in notes:
    #    raise exceptions.NotFound()
    #return note_repr(key)

if __name__ == '__main__':
    app.run()

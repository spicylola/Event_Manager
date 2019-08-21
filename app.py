import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from models import Events as EventsModel

@app.route('/')
def hello():
    return "Hello World!"

@app.route("/events", methods=['GET', 'PUT', 'POST'])
def cru_events(key):
    """
    Retrieve, update or create admin/regular users.
    """
    if request.method == 'POST':
       event_data = request.data.get("events")
       new_event = EventsModel(**event_data)
       db.session.add(events)
       db.session.commit()
       return event_data

    if request.method == 'PUT':
        event_data = str(request.data.get('events'))
        return event_data

    # TODO: Filter by USER ID
    #if request.method == 'GET':
    #if key not in notes:
    #    raise exceptions.NotFound()
    #return note_repr(key)

if __name__ == '__main__':
    app.run()

from app import db
from sqlalchemy.dialects.postgresql import JSON
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Events(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    created_by = db.Column(db.Integer)
    start_time = db.Column(db.DateTime, nullable=True)
    end_time = db.Column(db.DateTime, nullable=True)
    description = db.Column(JSON)
    location = db.Column(db.String())
    status = db.Column(db.String())

    def __repr__(self):
        return '<id {}>'.format(self.id)

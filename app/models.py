from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Unicode(100))
    body = db.Column(db.UnicodeText)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body

db.create_all()

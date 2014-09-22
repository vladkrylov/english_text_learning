from app import app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

db = SQLAlchemy(app)

class Text(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Unicode(100))
    body = db.Column(db.UnicodeText)

    def __init__(self, title=None, body=None):
        self.title = title
        self.body = body
        
    def __repr__(self):
        return "Text id %d\nTitle: %s" % (self.id, self.title)
        
class Tense(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), unique=True)
    short_name = db.Column(db.String(5), unique=True)
    
    def __init__(self, name=None):
        self.name = name
        
    def __repr__(self):
        return "Tense: %s\n Short name: %s" % (self.name, self.short_name)
        
class Phrase(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.Unicode(200), unique=True)
    
    text_id = db.Column(db.Integer, db.ForeignKey("text.id"))
    text = db.relationship('Text', backref='phrases')
    
    tense_id = db.Column(db.Integer, db.ForeignKey("tense.id"))
    tense = db.relationship('Tense', backref='phrases')
    
    def __init__(self, body=None, text=None, tense=None):
        self.body = body
        self.text = text
        self.tense = tense
    
    

    
db.create_all()

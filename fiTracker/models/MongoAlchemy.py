
from fiTracker import db

class User(db.Document):
    name = db.StringField()
    passwd = db.StringField()
    


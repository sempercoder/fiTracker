
from fiTracker import db
from flaskext.mongoalchemy import BaseQuery

class CustomBaseQuery(BaseQuery):
    def get_name(self, name):
        return self.filter(self.type.username == name)

class User(db.Document):
    query_class = CustomBaseQuery
    username = db.StringField()
    password = db.StringField()
    email = db.StringField()
    height = db.StringField()
    weight = db.StringField()
    

from schema import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # id, Username, Password
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)
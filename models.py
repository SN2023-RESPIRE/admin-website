from flask_login import UserMixin

from db import user_db


class User(UserMixin, user_db.Model):
    id = user_db.Column(user_db.Integer, primary_key=True)
    username = user_db.Column(user_db.String(32), unique=True)
    password = user_db.Column(user_db.String(128))
    name = user_db.Column(user_db.String(128))

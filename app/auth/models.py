from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5
from time import time
from flask import current_app as app
import jwt


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    is_confirmed = db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_token(self, expires_in=600):
        payload = {"user_id": self.id, "exp": time() + expires_in}
        token = jwt.encode(payload, app.config["SECRET_KEY"], algorithm="HS256")
        return token.decode("utf-8")

    @staticmethod
    def verify_token(token):
        try:
            payload = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"]
            )  # automatically check expire time
            id = payload["user_id"]
        except:
            return None
        user = User.query.get(id)
        if not user:
            return None
        return user

    def __repr__(self):
        return "<User {}>".format(self.username)

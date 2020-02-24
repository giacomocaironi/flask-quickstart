from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)

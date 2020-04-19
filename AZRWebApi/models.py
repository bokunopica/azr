from config.extensions import db


class BaseModel(db.Model):
    id = db.Column(db.Integer,primary_key=True)
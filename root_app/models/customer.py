from root_app.extensions import db

class Profile(db.Model):
    __table_args__ = {'schema':'local'}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    Gender = db.Column(db.String(80), unique=True, nullable=False)
    phonenumber = db.Column(db.String(255), nullable=False)
    active = db.Column(db.Boolean, default=True)
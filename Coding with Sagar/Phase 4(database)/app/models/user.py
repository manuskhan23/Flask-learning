from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(200),unique=True,nullable=False)
    post=db.relationship('Post',backref='author',lazy=True)
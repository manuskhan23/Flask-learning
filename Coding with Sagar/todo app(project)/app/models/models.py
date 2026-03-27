from app import db

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    password=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)

class Task(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    status=db.Column(db.String(20),nullable=False)
    due_date=db.Column(db.Date,nullable=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
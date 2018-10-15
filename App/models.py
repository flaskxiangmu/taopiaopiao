from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hello(db.Model):
     id = db.Column(db.Integer,primary_key=True,autoincrement=True)
     name = db.Column(db.String(64))
     age = db.Column(db.Integer)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)

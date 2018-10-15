from flask_sqlalchemy import SQLAlchemy

<<<<<<< HEAD
db = SQLAlchemy()
=======
db = SQLAlchemy()


class Hello(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    age = db.Column(db.Integer)
>>>>>>> 4d6f1f5d5571edb0c642df182c338c96d9c2a4b5

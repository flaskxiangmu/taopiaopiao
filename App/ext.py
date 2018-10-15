from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session


from App.models import db


def init_ext(app):
    # blue
    # app.register_blueprint(blueprint=blue)
    # migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)
    # session
    app.config['SECRET_KEY'] = '100'
    app.config['SESSION_TYPE'] = 'redis'

    Session(app=app)
    # sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost:3306/FlaskDay05'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app=app)


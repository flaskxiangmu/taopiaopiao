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
    db.init_app(app=app)


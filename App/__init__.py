from flask import Flask

from App import settings
from App.ext import init_ext


def create_app(Env_name):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(Env_name))
    init_ext(app)
    return app

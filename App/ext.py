from flask_migrate import Migrate
from flask_restful import Api
from flask_session import Session

from App.apis import Hello1, Cats, CatTest, CatTwo, CatThree
from App.models import db


def init_ext(app):
    #blue
    # app.register_blueprint(blueprint=blue)
    # migrate
    migrate = Migrate()
    migrate.init_app(app=app, db=db)
    #session
    app.config['SECRET_KEY']='100'
    app.config['SESSION_TYPE']='redis'

    Session(app=app)
    #sqlalchemy
    app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1234@localhost:3306/FlaskDay05'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
    db.init_app(app=app)

    #因为api能够路由，这时候就不用蓝图，也可以直接路由
    api = Api()
    #第一个参数是我们要操作的类
    #为什么为把Hello1写在了api中呢？因为增删该查都是在api中执行的
    api.add_resource(Hello1,'/hello1/')
    api.add_resource(Cats,'/cat/')
    api.add_resource(CatTest,'/cattest/')
    api.add_resource(CatTwo,'/cattwo/')
    api.add_resource(CatThree,'/catthree/')
    api.init_app(app=app)


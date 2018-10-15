from flask import  jsonify
from flask_restful import Resource, marshal_with, fields, reqparse

# blue = Blueprint('blue',__name__)
#
# @blue.route('/')
# def hello():
#     return '123'
from App.models import Cat

'''
1 api = Api()
2 api.add_resource(Hello1,'/hello1/')
3 api.init_app(app=app)


4 类继承Resource类

'''

class Hello1(Resource):
    def get(self):
        data={
            'msg':'我是get'
        }
        return jsonify(data)

    def post(self):
        data = {
            'msg': '我是post'
        }
        return jsonify(data)

    def delete(self):
        data = {
            'msg': '我是delete'
        }
        return jsonify(data)




cat_fields = {
    'msg':fields.String(default='jfdjklfjdskljfl'),
    'status':fields.String(attribute='xxx')
}



class CatTest(Resource):
    @marshal_with(cat_fields)
    def get(self):
        return {'xxx':'xxx'}



c_fields = {
    'id':fields.Integer,
    'name':fields.String,
    'age':fields.Integer
}

cats_fields = {
            'msg':fields.String,
            'status':fields.String,
            'cat':fields.Nested(c_fields) #Nested指的是嵌套
}

class Cats(Resource):
    #获取所有的猫  查询的是单个对象
    @marshal_with(cats_fields)
    def get(self):
        cat = Cat.query.first()
        data = {
            'msg':'ok',
            'status':'200',
            'cat':cat,
        }
        #如果已经是json数据格式了 那么就不需要jsonify方法了
        return data

cattwo_fields = {
            'msg': fields.String,
           'status': fields.String,
            # 'cats':fields.List(fields.Nested(c_fields))
            'cats':fields.Nested(c_fields)
}

class CatTwo(Resource):
    @marshal_with(cattwo_fields)
    def get(self):
       cats =  Cat.query.all()
       data = {
           'msg': 'ok',
           'status': '200',
           'cats': cats,
       }
       return data

#使用paser能够避免前端判断id是否存在，如果没有输入，检测到后就会及时提示id你必须写一下。
#获取一个parser对象
parser = reqparse.RequestParser()
#将参数存储到parser对象上  parser对象中包含了所有的请求参数
parser.add_argument('id',type=int,required=True,help='id你必须写一下')
parser.add_argument('name',type=str)
#将所有的参数都方到了parse对象上




# id = parse.get('id')

class CatThree(Resource):
    @marshal_with(cats_fields)
    def get(self):
        parse = parser.parse_args()
        id = parse.get('id')
        cat = Cat.query.get(id)
        data = {
            'msg':'ok',
            'status':'200',
            'cat':cat
        }
        return data



import flask_restful
from flask.json import jsonify


class Hello(flask_restful.Resource):

    def get(self):
        data = {
            'msg': 'ok',
            'status': 200,

        }
        return jsonify(data)

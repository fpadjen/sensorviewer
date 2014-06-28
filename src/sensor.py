import os
from flask import Flask, request, g, send_from_directory
from flask.ext import restful

from pymongo.errors import OperationFailure
from flask_pymongo import PyMongo
from functools import wraps

app = Flask(__name__, template_folder='../templates', static_folder='../static')
api = restful.Api(app)
app.config['MONGO_URI'] = os.environ.get('MONGOSOUP_URL', 'mongodb://localhost/sensor')
mongo = PyMongo(app)
app.debug = True

def remove_id(data):
        if '_id' in data:
            del data['_id']
        return data


def prepare_response(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data = f(*args, **kwargs)
        return remove_id(data)
    return decorated

@app.route('/bower_components/<path:filename>')
def custom_static(filename):
    return send_from_directory(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bower_components')), filename)

@app.route('/')
def index():
    return app.send_static_file('index.html')


class Point(restful.Resource):
    @prepare_response
    def post(self):
        print request.json
        uuid = mongo.db.points.insert(request.json)
        return mongo.db.points.find_one_or_404({'_id': uuid})

api.add_resource(Point, '/points/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 5000)))

from flask_restplus import Api
from flask import Blueprint
from app.main.controllers import *

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='Api Rest',
          doc='/docs')

api.add_namespace(test_ns, path='/')
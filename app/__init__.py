from flask_restplus import Api
from flask import Blueprint
from app.main.controllers import supermarket_ns
from app.main.controllers import category_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='Api Rest',
          doc='/docs')

api.add_namespace(supermarket_ns)
api.add_namespace(category_ns)
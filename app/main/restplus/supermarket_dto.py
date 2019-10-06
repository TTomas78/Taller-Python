from flask_restplus import Namespace
from flask_restplus import fields

class SuperMarketDto():
    api = Namespace('Supermarkets', description='Supermarket related operations', path='/')
    supermarket_post = api.model('supermarket',{
        'name': fields.String(description='Name of the supermarket', example='Supermarket 1'),
        'address': fields.String(description='Address of the supermarket', example='Fake Street 123'),
        'open_time': fields.String(description='Open Time', example='16:00'),
        'close_time': fields.String(description='Close Time', example='21:00')
    })
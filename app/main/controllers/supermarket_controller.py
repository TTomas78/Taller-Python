from flask import request
from flask_restplus import Resource
from app.main.restplus.supermarket_dto import SuperMarketDto

api = SuperMarketDto.api

@api.route('/supermarkets/')
class SupermarketListResource(Resource):
    @api.doc('get_all_supermarkets')
    def get(self):
        """A test_controller"""
        return True, 200


    @api.expect(SuperMarketDto.supermarket_post)
    @api.doc('create_supermarkets')
    def post(self):
        """A test_controller"""
        return True, 202
    
    


@api.route('/supermarkets/<int:supermarket_id>')
class SupermarketResource(Resource):
    @api.doc('get_supermarket_by_id')
    def get(self, supermarket_id):
        """A test_controller"""
        return True, 200

    @api.doc('get_supermarket_by_id')
    def put(self, supermarket_id):
        """A test_controller"""
        return True, 200


    @api.doc('get_supermarket_by_id')
    def delete(self, supermarket_id):
        """A test_controller"""
        return True, 200

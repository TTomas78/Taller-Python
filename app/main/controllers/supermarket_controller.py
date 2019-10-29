from flask import request
from flask_restplus import Resource
from marshmallow import ValidationError
from app.main.services.response_service import ResponseService
from app.main.schemas.supermarket_schema import SupermarketModelSchema
from app.main.restplus.supermarket_dto import SuperMarketDto
from app.main.services.supermarket_service import SupermarketService
from app.main.exceptions import ResourceAlreadyExistsException
from app.main.exceptions import ResourceNotFoundException

api = SuperMarketDto.api


@api.route('/supermarkets/')
class SupermarketListResource(Resource):
    @api.doc('get_all_supermarkets')
    def get(self):
        """A test_controller"""
        response_code = 200
        result = None
        supermarkets = SupermarketService.get_all()
        supermarket_schema = SupermarketModelSchema(many=True)
        result = supermarket_schema.dump(supermarkets)
        return result, response_code

    @api.expect(SuperMarketDto.supermarket_post)
    @api.doc('create_supermarkets')
    def post(self):
        """A test_controller"""
        response_service = ResponseService()
        response_code = 201
        result = None
        try:
            supermarket = SupermarketService.post(api.payload)
            supermarket_schema = SupermarketModelSchema()
            result = supermarket_schema.dump(supermarket)
        except ValidationError as error:
            response_code = 400
            response_service.add_messages(error.messages)
        except ResourceAlreadyExistsException as error:
            response_code = 400
            response_service.add_messages(error.message)
        return response_service.response(result), response_code


@api.route('/supermarkets/<int:supermarket_id>')
class SupermarketResource(Resource):
    @api.doc('get_supermarket_by_id')
    def get(self, supermarket_id):
        """A test_controller"""
        response_code = 200
        result = None
        try:
            supermarket = SupermarketService.get(supermarket_id)
            supermarket_schema = SupermarketModelSchema()
            result = supermarket_schema.dump(supermarket)
        except ResourceNotFoundException as error:
            response_code = 404
            result = error.message
        return result, response_code

    @api.expect(SuperMarketDto.supermarket_post)
    @api.doc('get_supermarket_by_id')
    def put(self, supermarket_id):
        """A test_controller"""
        response_code = 200
        result = None
        try:
            supermarket = SupermarketService.put(supermarket_id, api.payload)
            supermarket_schema = SupermarketModelSchema()
            result = supermarket_schema.dump(supermarket)
        except ResourceAlreadyExistsException as error:
            response_code = 400
            result = error.message
        except ResourceNotFoundException as error:
            response_code = 404
            result = error.message
        return result, response_code

    @api.doc('get_supermarket_by_id')
    def delete(self, supermarket_id):
        """A test_controller"""
        response_code = 200
        result = None
        try:
            SupermarketService.delete(supermarket_id)
        except ResourceNotFoundException as error:
            response_code = 404
            result = error.message
        return result, response_code

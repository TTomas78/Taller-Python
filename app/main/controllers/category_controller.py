from flask import request
from flask_restplus import Resource
from marshmallow import ValidationError
from app.main import ResponseService
from app.main.schemas.category_schema import CategoryModelSchema
from app.main.restplus.categories_dto import CategoriesDto
from app.main.services.category_service import CategoryService
from app.main.exceptions import ResourceAlreadyExistsException
from app.main.exceptions import ResourceNotFoundException

api = CategoriesDto.api


@api.route('/categories/')
class CategoryListResource(Resource):
    @api.doc('get_all_categories')
    def get(self):
        """A test_controller"""
        response_code = 200
        result = None
        categories = CategoryService.get_all()
        category_schema = CategoryModelSchema(many=True)
        result = category_schema.dump(categories)
        return ResponseService.response(result), response_code

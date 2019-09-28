from flask import request
from flask_restplus import Namespace
from flask_restplus import Resource
from app.main.models import TestingModel
from app.main.schemas import TestingModelSchema
from app.main.schemas import ContainTestingModelSchema
from app.main.exceptions import ResourceNotFoundException
api = Namespace('test', description='test related operations')


@api.route('tests')
class TestResourceList(Resource):
    @api.doc('get_all_tests')
    def get(self):
        """A test_controller"""
        return True, 200


@api.route('tests/<int:test_id>')
class TestResource(Resource):
    @api.doc('get_test_by_id')
    def get(self, test_id):
        """A test_controller"""
        try:
            test = TestingModel.query.get(test_id)
            if test is None:
                raise ResourceNotFoundException(test_id)
            test = TestingModelSchema().dump(test)
        except ResourceNotFoundException as error:
            return error.message, 404
        return test, 200

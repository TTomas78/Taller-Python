from marshmallow import fields
from app.main.models import TestingModel
from app.main.schemas import BaseSchema


class TestingModelSchema(BaseSchema):
    class Meta(BaseSchema):
        model = TestingModel
        fields = ('id', 'name', 'is_active', 'example_enum', 'contains')

    contains = fields.Nested('ContainTestingModelSchema', many=True)

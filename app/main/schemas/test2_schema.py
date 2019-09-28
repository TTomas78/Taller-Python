from marshmallow import fields
from app.main.models import ContainTestingModel
from app.main.schemas import BaseSchema


class ContainTestingModelSchema(BaseSchema):
    class Meta(BaseSchema):
        model = ContainTestingModel
        fields = ('id', 'name', 'is_active', 'testing_id', 'test')

    test = fields.Nested('TestModelSchema')
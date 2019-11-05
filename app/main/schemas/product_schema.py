from marshmallow import fields
from app.main.models import ProductModel
from app.main.schemas import BaseSchema


class ProductModelSchema(BaseSchema):
    class Meta(BaseSchema):
        model = ProductModel
        fields = ('id', 'name', 'category_id', 'category')

    category = fields.Nested('CategoryModelSchema', many=False)
from marshmallow import fields
from app.main.models import CategoryModel
from app.main.schemas import BaseSchema


class CategoryModelSchema(BaseSchema):
    class Meta(BaseSchema):
        model = CategoryModel
        fields = ('id', 'name', 'products')

    products = fields.Nested('ProductModelSchema',
                             many=True,
                             exclude=['category', 'category_id'])

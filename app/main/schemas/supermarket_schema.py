from datetime import time
from marshmallow import ValidationError
from marshmallow import fields
from marshmallow import post_load
from app.main.models import SupermarketModel
from app.main.schemas import BaseSchema


class SupermarketModelSchema(BaseSchema):
    class Meta(BaseSchema):
        model = SupermarketModel
        fields = ('id', 'name', 'address', 'open_time', 'close_time')

    open_time = fields.Time(format='%H:%M')
    close_time = fields.Time(format='%H:%M')

    # @post_load()
    # def post_load(self, data):
    #     if data.open_time > data.close_time:
    #         raise ValidationError(message={'Close_time is greather than open_time'})
    #     return data
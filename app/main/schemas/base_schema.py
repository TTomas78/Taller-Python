from app.main import ma
from app.main import db
from marshmallow import fields


class CommonSchema(ma.ModelSchema):
    class Meta:
        sqla_session = db.session


class BaseSchema(CommonSchema):
    class Meta(CommonSchema.Meta):
        fields = ('is_active', )

    is_active = fields.Boolean(default=True)
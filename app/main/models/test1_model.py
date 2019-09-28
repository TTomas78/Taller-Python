from app.main import db
from app.main.models.base_model import BaseModel
from app.main.models.enums import TEST_ENUM
from app.main.models.enums import TEST


class TestingModel(BaseModel):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    example_enum = db.Column(TEST_ENUM, server_default=TEST[0])
    contains = db.relationship(
        'ContainTestingModel',
        backref='test',
        primaryjoin=('and_('
                     'TestingModel.id==ContainTestingModel.testing_id,'
                     'ContainTestingModel.is_deleted==False)'))

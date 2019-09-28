from app.main.models.base_model import BaseModel
from app.main import db


class ContainTestingModel(BaseModel):
    __tablename__ = 'contains'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    testing_id = db.Column(db.Integer,
                           db.ForeignKey('tests.id',
                                         onupdate='CASCADE',
                                         ondelete='RESTRICT'),
                           nullable=False)

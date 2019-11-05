from app.main import db
from app.main.models.base_model import BaseModel


class CategoryModel(BaseModel):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    products = db.relationship(
        'ProductModel',
        primaryjoin=('and_('
                     'CategoryModel.id==ProductModel.category_id,'
                     'ProductModel.is_deleted==False)'),
        uselist=True)

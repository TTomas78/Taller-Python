from app.main import db
from app.main.models.base_model import BaseModel


class ProductModel(BaseModel):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    category_id = db.Column(db.Integer,
                            db.ForeignKey('categories.id',
                                          onupdate='CASCADE',
                                          ondelete='RESTRICT'),
                            nullable=False)
    category = db.relationship(
        'CategoryModel',
        primaryjoin=('and_('
                     'CategoryModel.id==ProductModel.category_id,'
                     'CategoryModel.is_deleted==False)'))

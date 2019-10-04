from app.main import db
from app.main.models.base_model import BaseModel


class SupermarketModel(BaseModel):
    __tablename__ = 'supermarkets'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    open_time = db.Column(db.Time(), nullable=False)
    close_time = db.Column(db.Time(), nullable=False)
    address = db.Column(db.String(100), nullable=False)

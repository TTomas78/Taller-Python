from app.main import db
from app.main.models import SupermarketModel
from app.main.schemas import SupermarketModelSchema
from app.main.repositories.supermarket_repository import SupermarketRepository


class SupermarketService():
    @staticmethod
    def post(payload):
        supermarket_schema = SupermarketModelSchema()
        supermarket = supermarket_schema.load(payload)
        SupermarketRepository.name_exists(supermarket.name)
        db.session.add(supermarket)
        db.session.commit()
        return supermarket
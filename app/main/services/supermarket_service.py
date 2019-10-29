from app.main import db
from app.main.models import SupermarketModel
from app.main.schemas import SupermarketModelSchema
from app.main.repositories.supermarket_repository import SupermarketRepository


class SupermarketService():
    @staticmethod
    def get_all():
        return SupermarketRepository.get_all()

    @staticmethod
    def get(supermarket_id):
        return SupermarketRepository.get(supermarket_id)

    @staticmethod
    def post(payload):
        supermarket_schema = SupermarketModelSchema()
        supermarket = supermarket_schema.load(payload)
        SupermarketRepository.name_exists(supermarket.name)
        db.session.add(supermarket)
        db.session.commit()
        return supermarket

    @staticmethod
    def put(supermarket_id, payload):
        supermarket = SupermarketRepository.get(supermarket_id)
        if supermarket.name != payload.get('name'):
            SupermarketRepository.name_exists(payload.get('name'))
        supermarket_schema = SupermarketModelSchema(instance=supermarket)
        supermarket = supermarket_schema.load(payload)
        db.session.commit()
        return supermarket

    @staticmethod
    def delete(supermarket_id):
        supermarket = SupermarketRepository.get(supermarket_id)
        supermarket.is_deleted = True
        db.session.commit()
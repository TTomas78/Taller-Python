from sqlalchemy import and_
from app.main.models import SupermarketModel
from app.main.exceptions import ResourceAlreadyExistsException
from app.main.exceptions import ResourceNotFoundException


class SupermarketRepository():
    @staticmethod
    def name_exists(name):
        supermarket = SupermarketModel.query.filter(
            SupermarketModel.name == name).first()
        if supermarket is not None:
            raise ResourceAlreadyExistsException()

    @staticmethod
    def get(supermarket_id):
        supermarket = SupermarketModel.query.filter(
            and_(SupermarketModel.id == supermarket_id,
                 SupermarketModel.is_deleted.is_(False))).first()
        if supermarket is None:
            raise ResourceNotFoundException(supermarket_id)
        return supermarket

    @staticmethod
    def get_all():
        return SupermarketModel.query.filter(
            SupermarketModel.is_deleted.is_(False)).all()

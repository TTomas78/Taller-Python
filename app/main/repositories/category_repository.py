from sqlalchemy import and_
from app.main.models import CategoryModel
from app.main.exceptions import ResourceAlreadyExistsException
from app.main.exceptions import ResourceNotFoundException


class CategoryRepository():
    # @staticmethod
    # def name_exists(name):
    #     supermarket = CategoryModel.query.filter(
    #         CategoryModel.name == name).first()
    #     if supermarket is not None:
    #         raise ResourceAlreadyExistsException()

    # @staticmethod
    # def get(supermarket_id):
    #     supermarket = CategoryModel.query.filter(
    #         and_(CategoryModel.id == supermarket_id,
    #              CategoryModel.is_deleted.is_(False))).first()
    #     if supermarket is None:
    #         raise ResourceNotFoundException(supermarket_id)
    #     return supermarket

    @staticmethod
    def get_all():
        return CategoryModel.query.filter(
            CategoryModel.is_deleted.is_(False)).all()

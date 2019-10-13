from app.main.models import SupermarketModel


class SupermarketRepository():
    @staticmethod
    def name_exists(name):
        supermarket = SupermarketModel.query.filter(
            SupermarketModel.name == name).first()
        if supermarket is not None:
            raise Exception('The name is beign used')

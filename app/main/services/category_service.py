from app.main.repositories.category_repository import CategoryRepository


class CategoryService():
    @staticmethod
    def get_all():
        return CategoryRepository.get_all()
from src.dto.category import Category
from src.repository.category_repository import CategoryRepository

class CategoryService:
    __category_repository = None

    def __init__(self, category_repository: CategoryRepository):
        self.__category_repository = category_repository

    def get_category(self, category_id: str) -> Category | None:
        if category_id is None: return None

        return self.__category_repository.get(category_id)

    def create_category(self, name: str) -> Category | None:
        if name is None: return None

        return self.__category_repository.get_or_create(name)

    def delete_category(self, category_id: str) -> Category | None:
        return self.__category_repository.delete(category_id)
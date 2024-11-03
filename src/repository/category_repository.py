import uuid

from src.dto import Category

class CategoryRepository:
    __categories = {}

    def get(self, category_id: str) -> Category:
        return self.__categories.get(category_id)

    def get_or_create(self, category_id: uuid) -> Category:
        category = self.__categories.get(category_id)
        if category: return category

        return self.create(category_id)

    def create(self, name: str) -> Category:
        category = Category(uuid.uuid4().hex, name)
        self.__categories[category.category_id] = category

        return category

    def delete(self, category_id: str) -> Category | None:
        category = self.get(category_id)
        if not category: return None

        return self.__categories.pop(category_id)

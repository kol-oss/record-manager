class Category:
    category_id = None
    name = None

    def __init__(self, category_id: str, name: str):
        self.category_id = category_id
        self.name = name
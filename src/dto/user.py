class User:
    user_id = None
    name = None

    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name
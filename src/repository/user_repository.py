import uuid

from src.dto import User

class UserRepository:
    __users = {}

    def get(self, user_id: str) -> User:
        return self.__users.get(user_id)

    def get_all(self):
        return self.__users.values()

    def get_or_create(self, user_id: str) -> User:
        user = self.get(user_id)
        if user: return user

        return self.create(user_id)

    def create(self, name: str) -> User:
        user = User(uuid.uuid4().hex, name)
        self.__users[user.user_id] = user

        return user

    def delete(self, user_id: str) -> User | None:
        user = self.get(user_id)
        if not user: return None

        return self.__users.pop(user_id)
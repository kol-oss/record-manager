from src.dto.user import User
from src.repository.user_repository import UserRepository

class UserService:
    __user_repository = None

    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def get_user(self, user_id: str) -> User | None:
        if user_id is None: return None

        return self.__user_repository.get(user_id)

    def get_all_users(self) -> list[User]:
        return list(self.__user_repository.get_all())

    def create_user(self, name: str) -> User | None:
        if name is None: return None

        return self.__user_repository.get_or_create(name)

    def delete_user(self, user_id: str) -> User | None:
        return self.__user_repository.delete(user_id)
from src.dto import Record
from src.repository import RecordRepository

class RecordService:
    __user_repository = None
    __category_repository = None
    __record_repository = None

    def __init__(
            self,
            user_repository: RecordRepository,
            category_repository: RecordRepository,
            record_repository: RecordRepository
    ):
        self.__user_repository = user_repository
        self.__category_repository = category_repository
        self.__record_repository = record_repository

    def get_record(self, record_id: str) -> Record | None:
        if record_id is None: return None

        return self.__record_repository.get(record_id)

    def get_all_records(self, user_id = None, category_id = None) -> list[Record]:
        filtered = []

        for record in self.__record_repository.get_all():
            if user_id is not None and record.user_id != user_id:
                continue

            if category_id is not None and record.category_id != category_id:
                continue

            filtered.append(record)

        return list(filtered)

    def create_record(self, user_id: str, category_id: str, value: int) -> Record | None:
        if self.__user_repository.get(user_id) is None: return None
        if self.__category_repository.get(category_id) is None: return None

        if value is None or value < 0: return None

        return self.__record_repository.create(user_id, category_id, value)

    def delete_record(self, record_id: str) -> Record:
        return self.__record_repository.delete(record_id)
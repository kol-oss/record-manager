import uuid

from src.dto import Record

class RecordRepository:
    __records = {}

    def get(self, record_id: str) -> Record:
        return self.__records.get(record_id)

    def get_all(self) -> list[Record]:
        return list(self.__records.values())

    def find(self, user_id: str, category_id: str) -> Record | None:
        for record in self.__records.values():
            if (record.user_id == user_id) and (record.category_id == category_id):
                return record

        return None

    def create(self, user_id: str, category_id: str, value: int) -> Record:
        found = self.find(user_id, category_id)
        if found is not None: return found

        record = Record(uuid.uuid4().hex, user_id, category_id, value)
        self.__records[record.record_id] = record

        return record

    def delete(self, record_id: str) -> Record | None:
        record = self.get(record_id)
        if not record: return None

        return self.__records.pop(record_id)
class Record:
    record_id = None
    user_id = None
    course_id = None
    value = 0

    def __init__(self, record_id: str, user_id: str, category_id: str, value: int):
        self.record_id = record_id
        self.user_id = user_id
        self.category_id = category_id
        self.value = value
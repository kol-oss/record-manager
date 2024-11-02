import uuid

class Record:
    user_id = None
    course_id = None
    value = 0

    def __init__(self, user_id, category_id, value):
        self.id = uuid.uuid4().hex
        self.user_id = user_id
        self.category_id = category_id
        self.value = value
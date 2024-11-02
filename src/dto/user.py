import uuid

class User:
    name = None

    def __init__(self, name):
        self.id = uuid.uuid4().hex
        self.name = name
from flask import Flask

app = Flask(__name__)

from dto import *

user = User("Nicholas")
print(user.id, user.name)

category = Category("Custom")
print(category.id, category.name)

record = Record(user.id, category.id, 10)
print(record.id, record.user_id, record.category_id, record.value)
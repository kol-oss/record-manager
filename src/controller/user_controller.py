from flask import request

from src import app
from src.service import UserService

from src.datasource import user_repository

USER_ROUTE = '/user'
user_service = UserService(user_repository)

@app.route(USER_ROUTE + 's', methods = ['GET'])
def get_users():
    users = user_service.get_all_users()

    return {"users": [user.__dict__ for user in users]}

@app.route(USER_ROUTE + '/<user_id>', methods = ['GET'])
def get_user(user_id):
    return user_service.get_user(user_id).__dict__

@app.route(USER_ROUTE, methods = ['POST'])
def create_user():
    user_data = request.get_json()
    name = user_data['name']
    if name is None or name == "": return {"message": "Please provide a name"}

    return user_service.create_user(name).__dict__

@app.route(USER_ROUTE + '/<user_id>', methods = ['DELETE'])
def delete_user(user_id):
    deleted_user = user_service.delete_user(user_id)

    if deleted_user is None: return None

    return deleted_user.__dict__
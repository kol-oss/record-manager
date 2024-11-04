from flask import request

from src import app
from src.service.category_service import CategoryService

from src.datasource import category_repository

CATEGORY_ROUTE = '/category'
category_service = CategoryService(category_repository)

@app.route(CATEGORY_ROUTE + '/<category_id>', methods = ['GET'])
def get_category(category_id):
    return category_service.get_category(category_id).__dict__

@app.route(CATEGORY_ROUTE, methods = ['POST'])
def create_category():
    category_data = request.get_json()
    name = category_data['name']
    if name is None or name == "": return {"message": "Please provide a name"}

    return category_service.create_category(name).__dict__

@app.route(CATEGORY_ROUTE + '/<category_id>', methods = ['DELETE'])
def delete_category(category_id):
    deleted_category = category_service.delete_category(category_id)

    if deleted_category is None: return None

    return deleted_category.__dict__
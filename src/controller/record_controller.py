from flask import request

from src import app
from src.service import RecordService

from src.datasource import user_repository
from src.datasource import category_repository
from src.datasource import record_repository

RECORD_ROUTE = '/record'
record_service = RecordService(user_repository, category_repository, record_repository)

@app.route(RECORD_ROUTE, methods = ['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')
    records = record_service.get_all_records(user_id, category_id)

    return {"records": [record.__dict__ for record in records]}

@app.route(RECORD_ROUTE + '/<record_id>', methods = ['GET'])
def get_record(record_id):
    return record_service.get_record(record_id).__dict__

@app.route(RECORD_ROUTE, methods = ['POST'])
def create_record():
    record_data = request.get_json()
    user_id = record_data['user_id']
    category_id = record_data['category_id']
    value = record_data['value']

    if user_id is None or user_id == "":
        return "Record must contain user_id", 403

    if category_id is None or category_id == "":
        return "Record must contain category_id", 403

    if value is None or value == "":
        return "Record must contain value", 403

    record = record_service.create_record(user_id, category_id, int(value))

    if not record: return "Provided data is not valid", 403

    return record.__dict__, 201

@app.route(RECORD_ROUTE + '/<record_id>', methods = ['DELETE'])
def delete_record(record_id):
    return record_service.delete_record(record_id).__dict__

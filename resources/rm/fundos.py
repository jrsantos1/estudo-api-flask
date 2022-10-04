from flask import jsonify
from flask_restful import Resource
from repository.repository_rm import multimesas_repository

class Multimesas(Resource):
    def get(self):
        return multimesas_repository.getAll()

class MultimesasFilter(Resource):
    def get(self, todo_id):
        return multimesas_repository.get_by_name(todo_id)

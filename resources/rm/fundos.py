from flask import jsonify
from flask_restful import Resource
from repository.repository_rm import multimesas_repository

class Multimesas(Resource):
    def get(self):
        return multimesas_repository.getAll()
    def post(self, parametro):
        return 

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from resources.rm.fundos import Multimesas, MultimesasFilter 


app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Multimesas, '/multimesas')
api.add_resource(MultimesasFilter,'/multimesas/<todo_id>')

if __name__ == '__main__':
    app.run(debug=True)


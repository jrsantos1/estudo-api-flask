from email import message
from flask import  Flask, jsonify, request, make_response
from flask_cors import CORS
from bd import Fundo

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)
# vincular funcao a url com @app.route

@app.route('/')
def home():
    return 'Olá Mundo aaa'

@app.route('/usuarios')
def usuarios():
    return 'você chegou na tela de usuários'

# é possível passar vários valores como ? string, paths, ints, uuid
@app.route('/usuarios/<int:id_usuario>', methods=['GET', 'POST'])
def usuarios_cadastro(id_usuario):
    if request.method == 'GET':
        return f'você chegou aqui: {id_usuario}'
    else:
        return 'voce nao e bem vindo'
    
    
@app.get('/testeget')
def acessogeet():
    return 'acesso get ok!!'

#retornando apissss!!!!!!!!!!!

#Getsssssss
@app.get('/api-jhon')
def api():
    return jsonify(Fundo)

#Postssssssss

@app.post('/api-jhon')
def api_post():
    
    fundo = request.json
    print(fundo)
    Fundo.append(fundo)
    print(Fundo)
    return make_response(jsonify(
        message = 'Dados cadastrado com sucesso!',
        dados = fundo
    ))

app.run()

#API - é um lugar para disponibilizar recursos e/ou funcionalidades
#1 .OBJETIVO - Criar um api de disponibiliza a conssulta , crição e exclusão de livros.
#2. URL Base - localhost
#3. Endpoints -
    # -localhost/livros (GET)
    # -localhost/livros/id (GET)
    # -localhost/livros/id (PUT)
    # -localhost/livros/id (DELETE)
#4. Quais recursos - LIVROS
from flask import Flask, jsonify, request

app = Flask(__name__)
livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedsra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'James Clear',
        'autor': 'Hábitos Atômicos'
    }
    
]
#Consultar (todos)
@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

#Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#Editar
@app.route('/livros/<int:id>', methods= ['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])
#Criar
@app.route('/livros', methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)

#Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livros(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
        return jsonify(livros)
app.run(port=500,host='localhost',debug=True)








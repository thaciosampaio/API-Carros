from flask import Flask, jsonify, request

app = Flask(__name__)

carros = [
    {
        'id': 1,
        'modelo': 'Mobi',
        'fabricante': 'Fiat'
    },
    {
        'id': 2,
        'modelo': 'Gol',
        'fabricante': 'Volkswagem'
    },
    {
        'id': 3,
        'modelo': 'Onix',
        'fabricante': 'Chevrolet'
    },
]

# Consultar (todos)
@app.route('/carros',methods=['GET'])
def obter_carros():
    return jsonify(carros)

# Consultar id
@app.route('/carros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for carro in carros:
        if carro.get ('id') == id:
            return jsonify(carro)

# Editar
@app.route('/carros/<int:id>',methods=['PUT'])
def editar_carro_por_id(id):
    carro_alterado = request.get_json()
    for indice,carro in enumerate(carros):
        if carro.get('id') == id:
            carros[indice].update(carro_alterado)
            return jsonify(carros[indice])

# Criar
@app.route('/carros',methods=['POST'])
def incluir_novo_carro():
    novo_carro = request.get_json()
    carros.append(novo_carro)

    return jsonify(carros)

# Excluir
@app.route('/carros/<int:id>',methods=['DELETE'])
def excluir_carro(id):
    for indice, carro in enumerate(carros):
        if carro.get('id') == id:
            del carros[indice]

    return jsonify(carros)

app.run(port=5000,host='localhost',debug=True)
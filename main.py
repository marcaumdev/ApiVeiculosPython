from flask import Flask, jsonify, make_response, request
from bd import Carros

app = Flask('carros')

@app.route('/carros', methods=['GET'])
def GetCarros():
    return Carros

@app.route('/carros/<int:id>', methods=['GET'])
def GetCarro(id):
    for carro in Carros:
        if carro['id'] == id:
            return jsonify(carro)
    return make_response(jsonify(mensagem= "Carro não encontrado!"))

@app.route('/carros', methods=['POST'])
def PostCarro():
    carroNovo = request.get_json()
    for carro in Carros:
        if carro['id'] == carroNovo['id']:
            return make_response(jsonify(mensagem=f"Carro com id {carroNovo['id']} já existe!"))
    Carros.append(carroNovo)
    return make_response(jsonify(mensagem= "Carro cadastrado com sucesso!", carro= carroNovo))

@app.route('/carros', methods=['PUT'])
def PutCarro():
    data = request.get_json()
    for carro in Carros:
        if 'id' in data:
            if carro['id'] == data['id']:
                if 'ano' in data:
                    if data['ano'] != carro['ano']:
                        carro['ano'] = data['ano']
                if 'marca' in data:
                    if data['marca'] != carro['marca']:
                        carro['marca'] = data['marca']
                if 'modelo' in data:
                    if data['modelo'] != carro['modelo']:
                        carro['modelo'] = data['modelo']
                return make_response(jsonify(mensagem= "Carro Atualizado com sucesso!", carro= carro))
    return make_response(jsonify(mensagem= "Carro não encontrado!"))

@app.route('/carros/<int:id>', methods=['DELETE'])
def DeleteCarro(id):
    for carro in Carros:
        if carro['id'] == id:
            Carros.remove(carro)
            return make_response(jsonify(mensagem= "Carro deletado com sucesso!", carro= carro))
    return make_response(jsonify(mensagem= "Carro não encontrado!"))


if __name__ == '__main__':
    app.run(port=5000, host='localhost')

from flask import Flask, jsonify, request
from bd import Carros

app = Flask('carros')

@app.route('/carros', methods=['GET'])
def GetCarros():
    return Carros

@app.route('/carros/<int:id>', methods=['GET'])
def GetCarro(id):
    for carro in Carros:
        if carro['id'] == id:
            return carro
    return f"Carro não encontrado!"

@app.route('/carros', methods=['POST'])
def PostCarro():
    data = request.get_json()
    for carro in Carros:
        if carro['id'] == data['id']:
            return f"Carro com id {data['id']} já existe!"
    Carros.append(data)
    return jsonify(data)

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
                return carro
    return f"Carro não encontrado!"

@app.route('/carros/<int:id>', methods=['DELETE'])
def DeleteCarro(id):
    for carro in Carros:
        if carro['id'] == id:
            Carros.remove(carro)
            return f"Carro com id {id} deletado!"
    return f"Carro não encontrado!"


if __name__ == '__main__':
    app.run()

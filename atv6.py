
from flask import Flask, jsonify, request

app = Flask(__name__)

carros_db = []
id = 0

@app.route("/carros")
def retornarcarros():
    return jsonify(carros_db)

@app.route("/carros", methods=["POST"])
def salvarcarros():
    global id
    id += 1
    dados = request.get_json()
    modelo = dados.get("modelo")
    marca = dados.get("marca")
    ano = dados.get("ano")

    carro = {"id": id, "modelo": modelo, "marca": marca, "ano": ano}
    carros_db.append(carro)

    return jsonify(carro)

@app.route("/carros/<int:id>", methods=["PUT"])
def editarcarro(id):
    dados = request.get_json()

    for carro in carros_db:
        if carro["id"] == id:
            carro["modelo"] = dados.get("modelo")
            carro["marca"] = dados.get("marca")
            carro["ano"] = dados.get("ano")
            return jsonify(carro), 200

    return jsonify({"Erro": "Carro não encontrado"}), 404

@app.route("/carros/<int:id>", methods=["DELETE"])
def excluircarro(id):
    for carro in carros_db:
        if carro["id"] == id:
            carros_db.remove(carro)
            return "", 204

    return jsonify({"erro": "Carro não encontrado"}), 404

app.run(debug=True)

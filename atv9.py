
from flask import Flask, jsonify, request

app = Flask(__name__)

restaurantes_db = []
id = 0

@app.route("/restaurantes")
def retornarrestaurantes():
    return jsonify(restaurantes_db)

@app.route("/restaurantes", methods=["POST"])
def salvarrestaurantes():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    tipo = dados.get("tipo")
    cidade = dados.get("cidade")

    restaurante = {"id": id, "nome": nome, "tipo": tipo, "cidade": cidade}
    restaurantes_db.append(restaurante)

    return jsonify(restaurante)

@app.route("/restaurantes/<int:id>", methods=["PUT"])
def editarrestaurante(id):
    dados = request.get_json()

    for restaurante in restaurantes_db:
        if restaurante["id"] == id:
            restaurante["nome"] = dados.get("nome")
            restaurante["tipo"] = dados.get("tipo")
            restaurante["cidade"] = dados.get("cidade")
            return jsonify(restaurante), 200

    return jsonify({"Erro": "Restaurante não encontrado"}), 404

@app.route("/restaurantes/<int:id>", methods=["DELETE"])
def excluirrestaurante(id):
    for restaurante in restaurantes_db:
        if restaurante["id"] == id:
            restaurantes_db.remove(restaurante)
            return "", 204

    return jsonify({"erro": "Restaurante não encontrado"}), 404

app.run(debug=True)

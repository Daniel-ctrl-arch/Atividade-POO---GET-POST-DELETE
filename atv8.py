
from flask import Flask, jsonify, request

app = Flask(__name__)

jogos_db = []
id = 0

@app.route("/jogos")
def retornarjogos():
    return jsonify(jogos_db)

@app.route("/jogos", methods=["POST"])
def salvarjogos():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    genero = dados.get("genero")
    ano = dados.get("ano")

    jogo = {"id": id, "nome": nome, "genero": genero, "ano": ano}
    jogos_db.append(jogo)

    return jsonify(jogo)

@app.route("/jogos/<int:id>", methods=["PUT"])
def editarjogo(id):
    dados = request.get_json()

    for jogo in jogos_db:
        if jogo["id"] == id:
            jogo["nome"] = dados.get("nome")
            jogo["genero"] = dados.get("genero")
            jogo["ano"] = dados.get("ano")
            return jsonify(jogo), 200

    return jsonify({"Erro": "Jogo não encontrado"}), 404

@app.route("/jogos/<int:id>", methods=["DELETE"])
def excluirjogo(id):
    for jogo in jogos_db:
        if jogo["id"] == id:
            jogos_db.remove(jogo)
            return "", 204

    return jsonify({"erro": "Jogo não encontrado"}), 404

app.run(debug=True)


from flask import Flask, jsonify, request

app = Flask(__name__)

musicas_db = []
id = 0

@app.route("/musicas")
def retornarmusicas():
    return jsonify(musicas_db)

@app.route("/musicas", methods=["POST"])
def salvarmusicas():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    artista = dados.get("artista")
    ano = dados.get("ano")

    musica = {"id": id, "nome": nome, "artista": artista, "ano": ano}
    musicas_db.append(musica)

    return jsonify(musica)

@app.route("/musicas/<int:id>", methods=["PUT"])
def editarmusica(id):
    dados = request.get_json()

    for musica in musicas_db:
        if musica["id"] == id:
            musica["nome"] = dados.get("nome")
            musica["artista"] = dados.get("artista")
            musica["ano"] = dados.get("ano")
            return jsonify(musica), 200

    return jsonify({"Erro": "Música não encontrada"}), 404

@app.route("/musicas/<int:id>", methods=["DELETE"])
def excluirmusica(id):
    for musica in musicas_db:
        if musica["id"] == id:
            musicas_db.remove(musica)
            return "", 204

    return jsonify({"erro": "Música não encontrada"}), 404

app.run(debug=True)

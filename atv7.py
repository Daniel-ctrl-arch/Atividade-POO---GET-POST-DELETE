
from flask import Flask, jsonify, request

app = Flask(__name__)

cidades_db = []
id = 0

@app.route("/cidades")
def retornarcidades():
    return jsonify(cidades_db)

@app.route("/cidades", methods=["POST"])
def salvarcidades():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    cidade = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    cidades_db.append(cidade)

    return jsonify(cidade)

@app.route("/cidades/<int:id>", methods=["PUT"])
def editarcidade(id):
    dados = request.get_json()

    for cidade in cidades_db:
        if cidade["id"] == id:
            cidade["nome"] = dados.get("nome")
            cidade["preco"] = dados.get("preco")
            cidade["categoria"] = dados.get("categoria")
            return jsonify(cidade), 200

    return jsonify({"Erro": "Cidade não encontrada"}), 404

@app.route("/cidades/<int:id>", methods=["DELETE"])
def excluircidade(id):
    for cidade in cidades_db:
        if cidade["id"] == id:
            cidades_db.remove(cidade)
            return "", 204

    return jsonify({"erro": "Cidade não encontrada"}), 404

app.run(debug=True)

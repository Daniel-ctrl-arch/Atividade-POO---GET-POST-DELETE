
from flask import Flask, jsonify, request

app = Flask(__name__)

produtos_db = []
id = 0

@app.route("/produtos")
def retornarprodutos():
    return jsonify(produtos_db)

@app.route("/produtos", methods=["POST"])
def salvarprodutos():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    preco = dados.get("preco")
    categoria = dados.get("categoria")

    produto = {"id": id, "nome": nome, "preco": preco, "categoria": categoria}
    produtos_db.append(produto)

    return jsonify(produto)

@app.route("/produtos/<int:id>", methods=["PUT"])
def editarproduto(id):
    dados = request.get_json()

    for produto in produtos_db:
        if produto["id"] == id:
            produto["nome"] = dados.get("nome")
            produto["preco"] = dados.get("preco")
            produto["categoria"] = dados.get("categoria")
            return jsonify(produto), 200

    return jsonify({"Erro": "Produto não encontrado"}), 404

@app.route("/produtos/<int:id>", methods=["DELETE"])
def excluirproduto(id):
    for produto in produtos_db:
        if produto["id"] == id:
            produtos_db.remove(produto)
            return "", 204

    return jsonify({"erro": "Produto não encontrado"}), 404

app.run(debug=True)

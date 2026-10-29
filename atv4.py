
from flask import Flask, jsonify, request

app = Flask(__name__)

funcionarios_db = []
id = 0

@app.route("/funcionarios")
def retornarfuncionarios():
    return jsonify(funcionarios_db)

@app.route("/funcionarios", methods=["POST"])
def salvarfuncionarios():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    cargo = dados.get("cargo")
    salario = dados.get("salario")

    funcionario = {"id": id, "nome": nome, "cargo": cargo, "salario": salario}
    funcionarios_db.append(funcionario)

    return jsonify(funcionario)

@app.route("/funcionarios/<int:id>", methods=["PUT"])
def editarfuncionario(id):
    dados = request.get_json()

    for funcionario in funcionarios_db:
        if funcionario["id"] == id:
            funcionario["nome"] = dados.get("nome")
            funcionario["cargo"] = dados.get("cargo")
            funcionario["salario"] = dados.get("salario")
            return jsonify(funcionario), 200

    return jsonify({"Erro": "Funcionário não encontrado"}), 404

@app.route("/funcionarios/<int:id>", methods=["DELETE"])
def excluirfuncionario(id):
    for funcionario in funcionarios_db:
        if funcionario["id"] == id:
            funcionarios_db.remove(funcionario)
            return "", 204

    return jsonify({"erro": "Funcionário não encontrado"}), 404

app.run(debug=True)


from flask import Flask, jsonify, request

app = Flask(__name__)

cursos_db = []
id = 0

@app.route("/cursos")
def retornarcursos():
    return jsonify(cursos_db)

@app.route("/cursos", methods=["POST"])
def salvarcursos():
    global id
    id += 1
    dados = request.get_json()
    nome = dados.get("nome")
    instituicao = dados.get("instituicao")
    duracao = dados.get("duracao")

    curso = {"id": id, "nome": nome, "instituicao": instituicao, "duracao": duracao}
    cursos_db.append(curso)

    return jsonify(curso)

@app.route("/cursos/<int:id>", methods=["PUT"])
def editarcurso(id):
    dados = request.get_json()

    for curso in cursos_db:
        if curso["id"] == id:
            curso["nome"] = dados.get("nome")
            curso["instituicao"] = dados.get("instituicao")
            curso["duracao"] = dados.get("duracao")
            return jsonify(curso), 200

    return jsonify({"Erro": "Curso não encontrado"}), 404

@app.route("/cursos/<int:id>", methods=["DELETE"])
def excluircurso(id):
    for curso in cursos_db:
        if curso["id"] == id:
            cursos_db.remove(curso)
            return "", 204

    return jsonify({"erro": "Curso não encontrado"}), 404

app.run(debug=True)

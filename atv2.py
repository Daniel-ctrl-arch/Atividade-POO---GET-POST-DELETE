from flask import Flask, jsonify, request

app = Flask(__name__)

alunos_db = []
id = 0
@app.route("/filmes")
def retornarfilmes():
    return jsonify(alunos_db)

@app.route("/alunos", methods=["POST"])
def salvaralunos():
    global id
    id +=1
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")

    aluno = {"id": id, "nome": nome, "curso": curso,"idade":idade}

    alunos_db.append(aluno)

    return jsonify(aluno)


@app.route("/alunos/<int:id>",methods = ["PUT"])
def editarfilme(id):
    dados = request.get_json()
    nome = dados.get("nome")
    curso = dados.get("curso")
    idade = dados.get("idade")
    for aluno in alunos_db:
        if aluno["id"] == id:
            aluno["nome"] = nome
            aluno["curso"] == curso
            aluno["idade"] == idade
            return jsonify(aluno), 200

    else:
        return jsonify ({"Erro":"Aluno não encontrado"}), 404

@app.route("/alunos/<int:id>",methods = ["DELETE"])
def excluirfilme(id):
   for aluno in alunos_db:
        if aluno["id"] == id:
            alunos_db.remove(aluno)
            return "", 204
        else:
            return jsonify({"erro": "Aluno não encontrado"}), 404 


app.run(debug=True)


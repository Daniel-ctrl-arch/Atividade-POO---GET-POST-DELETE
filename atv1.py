from flask import Flask, jsonify, request

app = Flask(__name__)

filmes_db = []
id = 0
@app.route("/filmes")
def retornarfilmes():
    return jsonify(filmes_db)

@app.route("/filmes", methods=["POST"])
def salvarfilmes():
    global id
    id +=1
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")

    filme = {"id": id, "nome": nome, "ano": ano,"diretor":diretor}

    filmes_db.append(filme)

    return jsonify(filme)


@app.route("/filmes/<int:id>",methods = ["PUT"])
def editarfilme(id):
    dados = request.get_json()
    nome = dados.get("nome")
    ano = dados.get("ano")
    diretor = dados.get("diretor")
    for filme in filmes_db:
        if filme["id"] == id:
            filme["nome"] = nome
            filme["ano"] == ano
            filme["diretor"] == diretor
            return jsonify(filme), 200

    else:
        return jsonify ({"Erro":"Filme não encontrado"}), 404

@app.route("/filmes/<int:id>",methods = ["DELETE"])
def excluirfilme(id):
   for filme in filmes_db:
        if filme["id"] == id:
            filmes_db.remove(filme)
            return "", 204
        else:
            return jsonify({"erro": "Filme não encontrado"}), 404      
    

        


app.run(debug=True)


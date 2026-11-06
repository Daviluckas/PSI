from flask import Flask, render_template


app = Flask(__name__)

livros = [
    {
        "id": 1,
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2022,
        "disponivel": True,
    },
    {
        "id": 2,
        "titulo": "Flask Web Development",
        "autor": "Miguel Grinberg",
        "ano": 2018,
        "disponivel": False,
    },
    {
        "id": 3,
        "titulo": "Automatize Tarefas Maçantes com Python",
        "autor": "Al Sweigart",
        "ano": 2019,
        "disponivel": True,
    },
]


@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/livros")
def listar_livros():
    return render_template("livros.html", livros=livros)

@app.route("/livros/<int:livro_id>")
def detalhe_livro(livro_id):
    livro_encontrado = None
    for livro in livros:
        if livro['id'] == livro_id:
            livro_encontrado = livro
            break
    if livro_encontrado is None:
        return 'livro não encontrado',404
    return render_template("detalhe.html", livro=livro_encontrado)

@app.route("/livros/disponiveis")
def disponiveis():
    livros_disponiveis = []

    for livro in livros:
        if livro['disponivel']:
            livros_disponiveis.append(livro)
    return render_template("livros.html", livros=livros_disponiveis)

if __name__ == "__main__":
    app.run(debug=True)
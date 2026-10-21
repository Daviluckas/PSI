from flask import Flask, redirect, render_template, request, url_for
from sqlalchemy import select

from database import SessionLocal
from models import Book, User

app = Flask(__name__)


@app.route("/")
def index():
    session = SessionLocal()
    usuarios = session.scalars(select(User)).all()
    livros = session.scalars(select(Book)).all()
    return render_template("index.html", usuarios=usuarios, livros=livros)


@app.route("/usuario/novo", methods=["POST", "GET"])
def new_user():
    if request.method == "POST":
        nome = request.form.get("nome", None)
        email = request.form.get("email", None)

        if nome and email:
            session = SessionLocal()
            usuario = session.scalars(select(User).where(User.email == email)).first()

            if not usuario:
                usuario_novo = User(nome=nome, email=email)
                session.add(usuario_novo)
                session.commit()

            return redirect(url_for("index"))

    return render_template("user_form.html")


@app.route("/livros/novo", methods=["POST", "GET"])
def new_book():
    session = SessionLocal()

    if request.method == "POST":
        titulo = request.form.get("titulo")
        user_id = request.form.get("user_id")

        if titulo and user_id:
            livro = session.scalars(select(Book).where(Book.titulo == titulo)).first()

            if not livro:
                livro_novo = Book(titulo=titulo, user_id=int(user_id))
                session.add(livro_novo)
                session.commit()

            return redirect(url_for("listar_livro"))

    usuarios = session.scalars(select(User)).all()
    return render_template("book_form.html", usuarios=usuarios)


@app.route("/livros/listar")
def listar_livro():
    session = SessionLocal()
    livros = session.scalars(select(Book).order_by(Book.titulo)).all()
    return render_template("index.html", livros=livros)


@app.route("/usuarios/listar")
def listar_usuarios():
    session = SessionLocal()
    usuarios = session.scalars(select(User).order_by(User.nome)).all()
    return render_template("index.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
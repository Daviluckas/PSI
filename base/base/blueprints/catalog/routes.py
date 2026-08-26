from flask import render_template, request
import models

from . import catalog_bp


@catalog_bp.route("/")
def index():
    q = request.args.get("q", "")
    livros = models.buscar_livros(q)
    return render_template(
        "catalog/index.html",
        livros=livros,
        q=q
    )


@catalog_bp.route("/livro/<int:livro_id>")
def ver_livro(livro_id):
    livro = models.buscar_livro(livro_id)

    if not livro:
        return "Livro não encontrado", 404

    resenhas = models.resenhas_do_livro(livro_id)

    return render_template(
        "catalog/livro.html",
        livro=livro,
        resenhas=resenhas
    )
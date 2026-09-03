from flask import request, redirect, url_for, session
import models

from . import reviews_bp


@reviews_bp.route(
    "/livro/<int:livro_id>/resenhar",
    methods=["POST"]
)
def resenhar(livro_id):
    if "usuario" not in session:
        return redirect(url_for("auth.login"))

    livro = models.buscar_livro(livro_id)

    if not livro:
        return "Livro não encontrado", 404

    texto = request.form.get("texto", "")
    nota = request.form.get("nota", "")

    if not texto or not nota:
        return "Texto e nota são obrigatórios", 400

    try:
        nota = int(nota)

        if nota < 1 or nota > 5:
            return "Nota deve ser entre 1 e 5", 400

    except ValueError:
        return "Nota inválida", 400

    nova_resenha = {
        "id": models.proximo_id_resenha,
        "livro_id": livro_id,
        "usuario": session["usuario"],
        "texto": texto,
        "nota": nota
    }

    models.resenhas.append(nova_resenha)
    models.proximo_id_resenha += 1

    return redirect(
        url_for("catalog.ver_livro", livro_id=livro_id)
    )
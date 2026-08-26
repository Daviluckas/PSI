from flask import render_template, request, redirect, url_for, session
import models

from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        nome = request.form.get("nome", "")
        senha = request.form.get("senha", "")

        usuario = None
        for u in models.usuarios:
            if u["nome"] == nome and u["senha"] == senha:
                usuario = u
                break

        if usuario:
            session["usuario"] = usuario["nome"]
            return redirect(url_for("catalog.index"))
        else:
            return render_template(
                "auth/login.html",
                erro="Usuário ou senha inválidos"
            )

    return render_template("auth/login.html", erro=None)


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("catalog.index"))
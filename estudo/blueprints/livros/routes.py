from flask import Blueprint, render_template, request, redirect, url_for, session

from sqlalchemy.orm import Session

from config import engine
from models import Livro


livros_bp = Blueprint('livros', __name__, url_prefix='/livros')


@livros_bp.route('/', methods=['GET', 'POST'])
def livros():
    db = Session(engine)
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        livro = Livro(titulo=titulo,autor=autor,usuario_id=session['usuario_id'])

        db.add(livro)
        db.commit()

        return redirect(url_for('livros.livros'))

    livros = db.query(Livro).all()
    return render_template('livros.html', livros=livros)
    
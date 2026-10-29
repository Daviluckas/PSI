from models import User
from flask import Blueprint, render_template, request
from config import engine
from sqlalchemy.orm import Session

users_bp = Blueprint('users',__name__,url_prefix='/users')


@users_bp.route('/', methods=['GET', 'POST'])
def cad_users():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        usuario = User(nome=nome, email=email, senha=senha)

        with Session(engine) as session:
            session.add(usuario)
            session.commit()
    return render_template('users.html')

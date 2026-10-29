from flask import Blueprint, render_template, request, redirect, url_for, session
from sqlalchemy.orm import Session
from config import engine
from models import User

login_bp = Blueprint('login',__name__,url_prefix='/login')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    senha = request.form['senha']

    with Session(engine) as db:
      usuario = db.query(User).filter_by(email=email).first()

      if usuario and usuario.senha == senha:
        session['usuario_id'] = usuario.id
        return redirect(url_for ('livros.livros'))

  return render_template('login.html')

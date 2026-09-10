from flask import Blueprint, render_template, request

users_bp = Blueprint('users',__name__,url_prefix='/users')


@users_bp.route('/', methods=['GET', 'POST'])
def cad_users():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        print(nome)
        print(email)
        print(senha)

    return render_template('users.html')

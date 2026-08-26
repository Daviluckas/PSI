from flask import Flask, render_template, request, redirect, url_for, session
import models

app = Flask(__name__)
app.secret_key = 'atividade01'

@app.route('/')
def index():
    q = request.args.get('q', '')
    livros = models.buscar_livros(q)
    return render_template('index.html', livros=livros, q=q)

@app.route('/livro/<int:livro_id>')
def livro_detalhe(livro_id):
    livro = models.buscar_livro(livro_id)
    if not livro:
        return "Livro não encontrado", 404
    resenhas = models.resenhas_do_livro(livro_id)
    return render_template('livro.html', livro=livro, resenhas=resenhas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form.get('nome', '')
        senha = request.form.get('senha', '')
        
        usuario = None
        for u in models.usuarios:
            if u['nome'] == nome and u['senha'] == senha:
                usuario = u
                break
        
        if usuario:
            session['usuario'] = usuario['nome']
            return redirect(url_for('index'))
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos')
    
    return render_template('login.html', erro=None)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/livro/<int:livro_id>/resenhar', methods=['POST'])
def resenhar(livro_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    
    livro = models.buscar_livro(livro_id)
    if not livro:
        return "Livro não encontrado", 404
    
    texto = request.form.get('texto', '')
    nota = request.form.get('nota', '')
    
    if not texto or not nota:
        return "Texto e nota são obrigatórios", 400
    
    try:
        nota = int(nota)
        if nota < 1 or nota > 5:
            return "Nota deve ser entre 1 e 5", 400
    except ValueError:
        return "Nota inválida", 400
    
    nova_resenha = {
        'id': models.proximo_id_resenha,
        'livro_id': livro_id,
        'usuario': session['usuario'],
        'texto': texto,
        'nota': nota
    }
    models.resenhas.append(nova_resenha)
    models.proximo_id_resenha += 1
    
    return redirect(url_for('livro_detalhe', livro_id=livro_id))

if __name__ == '__main__':
    app.run(debug=True)
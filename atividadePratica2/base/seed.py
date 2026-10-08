from models import Autor, Livro


def popular_banco(session, autores, livros):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    # TODO: crie pelo menos 3 autores.
    # TODO: crie pelo menos 6 livros.
    # TODO: inclua livros disponíveis e indisponíveis.
    # TODO: use session.add ou session.add_all e finalize com session.commit().

    autores = [
        Autor(id=1, nome="dlleon", pais="Brasil"),
        Autor(id=2, nome="kallil", pais="Arábia Saudita"),
        Autor(id=3, nome="lopes", pais="Angola"),
        Autor(id=4, nome="lucas", pais="Qatar"),
    ]

    livros = [
        Livro(id=1, titulo="A História de Romerito", autor='dlleon', ano=1987, disponivel=True),
        Livro(id=2, titulo="Romerito, Primeira corrida", autor='lopes', ano=1990, disponivel=False),
        Livro(id=3, titulo="Romerito do Corre ao Adizero", autor='dlleon', ano=1997, disponivel=True),
        Livro(id=4, titulo="Romerito o Oponente Agora é Outro", autor='kallil', ano=2001, disponivel=False),
        Livro(id=5, titulo="Príncipe da Rodagem", autor='lucas', ano=2012, disponivel=False),
        Livro(id=6, titulo="Romerito, Última Corrida", autor='lucas', ano=2018, disponivel=True),
        Livro(id=7, titulo="O Rei da Rodagem", autor='lucas', ano=2025, disponivel=False),
    ]
    pass
    session.all(autores)
    session.all(livros)
    session.commit()
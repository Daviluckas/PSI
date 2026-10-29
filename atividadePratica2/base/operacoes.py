from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Livro

def emprestar_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalars(stmt).all()

    if livro:
        if livro.disponivel:
            livro.disponivel == False
            print('livro ${titulo}')
            session.commit()
            if livro.disponivel == False:
                print('Livro indisponível')
    else:print('livro não existe')

    """Marque um livro como indisponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver indisponível, exiba uma mensagem.
    # TODO: se estiver disponível, altere disponivel para False e faça commit.
    pass


def devolver_livro(session, titulo):
    stmt = select(Livro).where(Livro.titulo == titulo)
    livro = session.scalars(stmt).all()

    if livro:
        if livro.disponivel:
            livro.disponivel == True
            print('livro disponível ${titulo}')
            session.commit()
            if livro.disponivel == True:
                print('Livro disponível')
    else: print('livro não existe')
    
    """Marque um livro como disponível."""
    # TODO: busque o livro pelo título.
    # TODO: se o livro não existir, exiba uma mensagem.
    # TODO: se já estiver disponível, exiba uma mensagem.
    # TODO: se estiver indisponível, altere disponivel para True e faça commit.
    pass

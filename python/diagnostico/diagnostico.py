"""Base da prática diagnóstica de fundamentos de Python.

Complete as funções marcadas e execute este arquivo depois de cada alteração.
"""


LIVROS = [
    {"id": 1, "titulo": "Python", "disponivel": True, "quantidade": 2},
    {"id": 2, "titulo": "Flask", "disponivel": False, "quantidade": 0},
    {"id": 3, "titulo": "SQLAlchemy", "disponivel": True, "quantidade": 1},
]


def calcular_total(quantidade, preco):
    # Tarefa 1: retorne quantidade multiplicada por preco.

    return quantidade * preco


def normalizar_email(email):
    # Tarefa 2: remova espacos das extremidades e converta para minusculas.

    email_identado = email.strip().lower()
    return email_identado


def validar_nota(nota):
    # Tarefa 3: aceite valores entre 0 e 10, inclusive.

    if 0 < nota < 10:
        return True
    else: 
        return False


def somar_disponiveis(livros):
    # Tarefa 4: some a quantidade dos livros disponiveis.

    soma = 0

    for l in livros :
        if l['disponivel']:
            soma += l['quantidade']

    return soma
    


def titulos_disponiveis(livros):
    # Tarefa 5: retorne uma lista com os titulos disponiveis.
    lista2 = []
    for l in livros:
        if l['disponivel']:
            lista2.append(l)
    return lista2
    

def nome_usuario(usuario):
    # Tarefa 6: retorne o nome ou "desconhecido" se a chave nao existir.

    if "nome" in usuario:
        return usuario["nome"]
    else:
        return print('Desconhecido')


def buscar_livro(livros, livro_id):
    # Tarefa 7: retorne o livro com o id ou None.

    for livro in livros:
        if livro["id"] == livro_id:
            return livro
      
    return None


def converter_idade(texto):
    # Tarefa 8: converta para inteiro; em caso de erro, retorne None.~
    try: 
        return int(texto)
    except ValueError:
        return None



class Livro:
    # Tarefa 10: adicione o atributo autor ao objeto.
    def __init__(self, titulo):
        self.titulo = titulo


def executar_testes():
    """Mostra casos de teste para orientar a verificacao manual."""
    print("Tarefa 1:", calcular_total(2, 10.5))
    print("Tarefa 2:", normalizar_email("  ALUNO@EXEMPLO.COM "))
    print("Tarefa 3:", validar_nota(7), validar_nota(11))
    print("Tarefa 4:", somar_disponiveis(LIVROS))
    print("Tarefa 5:", titulos_disponiveis(LIVROS))
    print("Tarefa 6:", nome_usuario({"nome": "Ana"}))
    print("Tarefa 7:", buscar_livro(LIVROS, 2))
    print("Tarefa 8:", converter_idade("18"), converter_idade("x"))

    livro = Livro("Python")
    print("Tarefa 10:", livro.titulo)


if __name__ == "__main__":
    executar_testes()

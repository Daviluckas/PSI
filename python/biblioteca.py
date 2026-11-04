livros = [
{
"id": 1,
"titulo": "Python Fluente",
"autor": "Luciano Ramalho",
"ano": 2022,
"disponivel": True
},
{
"id": 2,
"titulo": "Flask Web Development",
"autor": "Miguel Grinberg",
"ano": 2018,
"disponivel": False
},
{
"id": 3,
"titulo": "Automatize Tarefas Maçantes com Python",
"autor": "Al Sweigart",
"ano": 2019,
"disponivel": True
}
]

#É POSSÍVEL QUE DÊ ALGUM ERRO NA ÚLTIMA QUESTÃO NA HORA DE RODAR O CÓDIGO PELO FATO DAS VARIÁVEIS TEREM O NOME IGUAL EM ALGUMAS QUESTÕES
#SE NÃO DER, DESCONSIDERE A MENSAGEM ACIMA

#Perguntas

#1- livros é uma lista
#2- livros[0] quer dizer que está pegando o primeiro item da lista livros, pois o indice zero representa o primeiro item de uma lista.
#3- livros[1]["titulo"]
#4- False
#5- três livros 

#Prática
print(" Parte prática ".center(70, "="))

# 1-
print("-"*70)
print(" Questão 1 ".center(70, "-"))
cont = 0
for livro in livros:
    cont += 1
    print(f"{cont}- {livro['titulo']} ({livro['autor']})")
print("-"*70)

# 2- 
print(" Questão 2 ".center(70, "-"))
for livro in livros:
    print(f"- {livro['titulo']}")
print("-"*70)

# 3-
print(" Questão 3 ".center(70, "-"))
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
print(f"Quantidade disponível: {quantidade_disponiveis}")
print("-"*70)

# 4- 
print(" Questão 4 ".center(70, "-"))
id_buscado = 99
livro_encontrado = None

for livro in livros:
    if id_buscado == livro['id']:
        livro_encontrado = livro

if livro_encontrado is not None:
    print(f"{cont}- {livro['titulo']} ({livro['autor']})")
else:
    print("Livro não encontrado!")
print("-"*70)

# 5-
print(" Questão 5 ".center(70, "-"))
livros[1]['disponivel'] = True
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
print(f"Quantidade disponível: {quantidade_disponiveis}")
print("-"*70)

# 6-
print(" Questão 6 ".center(70, "-"))
novo_livro = {
    "id": 4,
    "titulo": "Programacao Python",
    "autor": "Autor da turma",
    "ano": 2026,
    "disponivel": True
}
livros.append(novo_livro)
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
    quantidade_total = len(livros)
print(f"Quantidade disponível: {quantidade_disponiveis}")
print(f"Quantidade total: {quantidade_total}")
print("-"*70)

# 7- 
print(" Questão 7 ".center(70, "-"))
livro_novo = {
    "id": 5,
    "titulo": "Introducao a Web",
    "autor": "Autora da turma"
}
livros.append(livro_novo)
for livro in livros:
    status = livro.get("disponivel", "nao informada")
    print(f"Titulo: {livro['titulo']} Disponibilidade: {status}")
print("-"*70)

# 8-
print(" Questão 8 ".center(70, "-"))
titulos_disponiveis = []
for livro in livros:
    if livro["disponivel"]:
        titulos_disponiveis.append(livro['titulo'])
print(titulos_disponiveis)
#A rota estaria enviando para livros.html apenas os titulos dos livros que estão disponíveis
print("-"*70)
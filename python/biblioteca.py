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

#Perguntas

#1- livros é uma lista
#2- livros[0] quer dizer que está pegando o primeiro item da lista livros, pois o indice zero representa o primeiro item de uma lista.
#3- livros[1]["titulo"]
#4- False
#5- três livros 

#Prática

# 1-
cont = 0
for livro in livros:
    cont += 1
    print(f"{cont}- {livro['titulo']} ({livro['autor']})")

# 2- 
for livro in livros:
    print(f"- {livro['titulo']}")

# 3-
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
print(f"Quantidade disponível: {quantidade_disponiveis}")

# 4- 
id_buscado = 99
livro_encontrado = None

for livro in livros:
    if id_buscado == livro['id']:
        livro_encontrado = livro

if livro_encontrado is not None:
    print(f"{cont}- {livro['titulo']} ({livro['autor']})")
else:
    print("Livro não encontrado!")

# 5-
livros[1]['disponivel'] = True
quantidade_disponiveis = 0
for livro in livros:
    if livro["disponivel"]:
        quantidade_disponiveis += 1
print(f"Quantidade disponível: {quantidade_disponiveis}")

# 6-
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

# 7- 
livro_novo = {
    "id": 5,
    "titulo": "Introducao a Web",
    "autor": "Autora da turma"
}
livros.append(livro_novo)
for livro in livros:
    status = livro.get("disponivel", "nao informada")
    print(f"Titulo: {livro['titulo']} Disponibilidade: {status}")

titulos_disponiveis = []
for livro in livros:
    if livro["disponivel"]:
        titulos_disponiveis.append(livro['titulo'])
print(titulos_disponiveis)
#A rota estaria enviando apenas os titulos dos livros que estão disponíveis
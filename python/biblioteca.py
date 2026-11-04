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

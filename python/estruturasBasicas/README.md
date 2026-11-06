PARTE 1 - CONHECENDO A BASE

1. Qual arquivo cria o objeto Flask?
2. Qual variável guarda a lista de livros?
3. Qual é o tipo de livros ?
4. Qual é o tipo de livros[0] ?
5. Qual rota é exibida quando abrimos / ?
6. O que render_template("inicio.html") faz?

-Respostas-
1- app.py
2- livros
3- uma lista de dicionários
4- o primeiro dicionário da lista
    {
        "id": 1,
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2022,
        "disponivel": True,
    }

5- inicio.html
6- redenriza o template/página inicio.html 


QUESTÕES DE REFLEXÃO

1. Qual é a entrada da rota /livros ?
2. Qual é o processamento realizado pela função listar_livros ?
3. Qual é a saída dessa rota?
4. Em que momento o for do Python é usado?
5. Em que momento o for do Jinja é usado?
6. Qual é a diferença entre livro["titulo"] e livros[0] ?
7. Por que a rota de detalhes recebe <int:livro_id> ?
8. O que significa retornar o status 404 ?
9. Por que o livro encontrado pode ser None ?
10. O que aconteceria se os dados fossem enviados para o template sem livros=livros ?

-Respostas-

1- /livros
2- mostra todos os livros que estão dentro da lista
3- a página livros.html
4- é usado quando se precisa percorrer uma lista para saber seu elementos ou buscá-los
5- é usado para percorrer a lista e mostrar seus elementos na página html
6- livro['titulo'] vai mostrar somente o título dos livros, nesse caso de todos os livros. Já livros[0] vai pegar o primeiro elemento da lista
7- por que nesse caso, só se usa essa rota para todos os livros buscando pelo id. Então para não ter que criar outra rota, muda-se apenas o id do livro que deve ser buscado
8- quer dizer que aquela página não foi encontrada
9- por que ele vai receber posteriormente um "valor" nesse caso 'livro'. Porém caso o livro não seja encontardo, retorna None
10- daria erro. Por que para mostrar os dados da variável, é necessário que ela seja chamada. Por que o html procura essa variável para poder usa-la.
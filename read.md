# Comandos Python

- Para escrever a palavra entre aspas
    print('"Palavra"')

- Imprimir texto igual está escrito
    print(""" a
    Dona aranha
    subiu pela parede""")

- Verificar o que um código faz
    help(NomeComando)

- Funções embutidas do python
    https://docs.python.org/3/library/functions.html

- Para saber a quantidade de caracteres em uma string
    len('palavra')

- Tornar tudo maiúsculo
    variavel.upper()

- Atribuição composta
    a, b = b, a + b

# Vetores
    - Adicionar item a array
         - No final: array.append(n)
         - Em outra posição: array.insert(indice, 'item')
    - Organizar
        array.sort()
    - Descrever funções
        dir.array()
    - Remover item
        - Pelo nome: predio.remove(item) 
        - Pelo índice: del predio[2]
    - Tamanho da array
        len(array)
    - Último item
        array[-1]
    - Inverter a order
        array.reverse()

# Funções de uma string
    - Substituir algum caractere por outro
        string.replace('carac a ser substituido', 'o que irá ir no lugar')
    - Mudar tudo para minúscula
        string.lower()
    - Separar palvras do texto
        texto.split() 
        - por algo específico: texto.split(", ")

# Random
    - Números aleatórios em um intervalo 
        random.radint(1, 100)
    - Quantidade determinada de números aleatórios em um intervalo 
        random.sample(range(100), 40)
                                   ^quantidade

    - Sortear numa array (string)
        random.choice(array)
        - Mais de um: random.sample(nomes, 2)
    
while n - 2 < count:
    a,b = a, a+b

MDC
    a - 21
    b - 15

    while a % b != 0
        a,b = b, a % b
para entregas - 
arquivo txt (bloco de notas) único 
fmasanori@gmail.com 
com seu nome completo e turma 
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
    
# For 
    - Percorrer um elemento 
        for p in texto:
            print(p)

    -Achar um elemento dentro de um conjunto 
        Ex: Última ou primeira letra pertence a palavra 'python' 
                for p in texto: 
                    if p[0] in 'python' or p [-1] in 'python': 
                        print(p) 
        
        - Sempre tranformar em string para achar; O not in é para não pertencer ao conjunto
            for k in range (18644, 33088):
                if '2' in str(k) and '7' not in str(k):
                    print(k)

# Arquivo
    - Abrir arquivo
        open(caminhoArquivo) /* Control Space pra mostrar arquivos */

# Range
    - Imprime uma certa sequência de números. range(inicio, fim, de quantos em quantos)
        for k in range(1, 10, 2): #Imprime de 1 á 9 de dois em dois !Sempre para um número antes
            print(k)

# Funções
    Uma parte do código que irá ser salva na mémoria e poderá ser executada mais vezes. Tem q usar o print função() para mostrar o resultado
        def nomeFunção(param):
        
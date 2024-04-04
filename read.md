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
        array.sort() - ordem crescente
        array.sort(reverse=True) - decrescente
    - Descrever funções
        dir.array()
    - Remover item
        - Pelo nome: predio.remove(item) 
        - Pelo índice: array.pop(indice) ~Se não indicado removerá o último
        - Limpar lista: array.clear
    - Tamanho da array
        len(array)
    - Último item
        array[-1]
    - Inverter a order 
        array.reverse()
    - Procurar um elemento específico e contar sua ocorrência
        array.count('elemento')
    - Mostrar o menor e máximo elemento da lista
        min(array) ou max(array)
    - Somar elementos de uma lista
        sum(array)
    - Index de um elemento
        array.index('elemento')
    - Mostrar Indice e Elemento ao mesmo tempo
        for indice, valor in enumerate(array):

# Funções de uma string
    - Substituir algum caractere por outro
        string.replace('carac a ser substituido', 'o que irá ir no lugar')
    - Mudar tudo para minúscula
        string.lower()
    - Separar palvras do texto
        texto.split() 
        - por algo específico: texto.split(", ")
    - Strings também possuem índice, logo, é possível pegar letras especifícas por sua posição
        string[indice]

# Slicing - Slice
    O método slice consiste em "fatiar" uma lista ou string, ou seja, retorna uma parte específica do item. Para fazer isso deve ser passado o inicio e fim dentro do índice
        string[inicio:fim]
    Por padrão, se nada for indicado (string[:]), será gerado uma cópia pois vai do ínicio ao fim
    Exemplos:
    s[:n] retorna os caracteres da posição 0 até a posição n-1 de s.
    s[n:] retorna os caracteres da posição n até o final de s.
        
# Random
    - Números aleatórios em um intervalo 
        random.radint(1, 100)
    - Quantidade determinada de números aleatórios em um intervalo 
        random.sample(range(100), 40)
                                   ^quantidade

    - Sortear numa array (string)
        random.choice(array)
        - Mais de um: random.sample(nomes, 2)

    - Embaralhar uma lista/array
        random.shuffle(nomeArray)
    
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
    Uma parte do código que irá ser salva na mémoria e poderá ser executada mais vezes. Tem q usar o print função() para mostrar o resultado. Argumentos é oq é enviado e oq é recebido o parametro (mema coisa)
        def nomeFunção(param):
    Os parametros podem receber valores default, pra no caso de não ser passado todos os argumentos. Ex:
        def IMC (altura, nome = "Prezado(a)")
        
# Matriz
    Uma lista composta por outras listas. O indice da matriz são suas linhas e o indice da lista interna as colunas.
        M = [[10, 2], [7, 9], [21, 3]] 3 LINHAS 
    COLUNAS:  0,  1    0, 1    0,  1
    - Para acessar um elemento
        M[[LINHA][COLUNA]]
    - Inserir lista 
        M.append(lista)

# Dicionário
    Lista que contém chave e um valor. Nota: O valor pode ser qualquer tipo de dado
        nome_dic = {<chave>:<valor>} 
        ex: contato = {'1299784':'Camila','12987754':'Amanda'}
    - Retornar um elemento
        - O valor: dic['nomeChave'] ou dic.get('nomeChave') ou dic.values()
        - A chave: dic.keys()
        - Tudo: dic.items()
    - Adicionar novo elemento. Nota: Não pode haver chaves iguais, caso ocorrer update em uma chave já existente ele atualiza
        contato.update({'123354','Paola'})
    - Organiza os itens
        sorted(dic.items())
        -> pode ter o parâmetro para organizar por algo específico: key=parametro
            o paramêtro pode receber uma função, como itemgetter (importado da biblioteca operator) ou uma própria criada logo em seguida (o lambda). ex: key=lambda item: item[1] (organiza pelo primeiro item)
    - Copiar o dicionario
        dic.copy()
    - Remover
        - Item: dic.pop("chave") ou dic.popitem()
        - Apaga tudo: dic.clear()
    
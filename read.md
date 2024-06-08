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
    - Adicionar algo ao final de cada item
        string = '.'.join(str)
        - Transforma em string = ''.join(array)

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
    - Achar a posição de um caractere ou inicio de uma sequência
        string.find('caracteres')
    - Remover espaços em branco
        string.strip()

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
    - Ler arquivo - automaticamente fecha o arquivo
        with open('surf.txt') as f:
            print(f.read())

# Range
    - Imprime uma certa sequência de números. range(inicio, fim, de quantos em quantos)
        for k in range(1, 10, 2): #Imprime de 1 á 9 de dois em dois !Sempre para um número antes
            print(k)

# Funções
    Uma parte do código que irá ser salva na mémoria e poderá ser executada mais vezes. Tem q usar o print função() para mostrar o resultado. Argumentos é oq é enviado e oq é recebido o parametro (mema coisa)
        def nomeFunção(param):
    Os parametros podem receber valores default, pra no caso de não ser passado todos os argumentos. Ex:
        def IMC (altura, nome = "Prezado(a)")
    Argumentos podem ser args normal -> por posição, indicado por * ou kwargs que são dicionarios, indicados por **, recebem nome e valor
        
# Matriz
    Uma lista composta por outras listas. O indice da matriz são suas linhas e o indice da lista interna as colunas.
        M = [[10, 2], [7, 9], [21, 3]] 3 LINHAS 
    COLUNAS:  0,  1    0, 1    0,  1
    - Para acessar um elemento
        M[[LINHA][COLUNA]]
    - Inserir lista 
        M.append(lista)

# Dicionário
    Lista que contém chave e um valor. Nota: O valor pode ser qualquer tipo de dado mas a chave precisa ser imutavel
        nome_dic = {<chave>:<valor>} 
        ex: contato = {'1299784':'Camila','12987754':'Amanda'}
    - Retornar um elemento
        - O valor: dic['nomeChave'] ou dic.get('nomeChave') ou dic.values()
        - A chave: dic.keys()
        - Tudo: dic.items()
    - Adicionar novo elemento. 
        contato.update({'123354','Paola'}) -> Nota: Não pode haver chaves iguais, caso ocorrer update em uma chave já existente ele atualiza
        ou
        dic.setdefault(chave, valor) -> caso já existir a chave não altera
    - Organiza os itens
        sorted(dic.items())
        -> pode ter o parâmetro para organizar por algo específico: key=parametro
            o paramêtro pode receber uma função, como itemgetter (importado da biblioteca operator) ou uma própria criada logo em seguida (o lambda). ex: key=lambda item: item[1] (organiza pelo primeiro item)
        !** LAMBDA: Uma função que só será executada uma vez, não exige que seja criada de fato (com def e tals). Lambda é uma palavra reservada do python para isso. Funciona igual o list comprehension
            lambda itemRetornado : ações da função
            Ex: lambda x: x % 2 == 0
    - Copiar o dicionario
        dic.copy()
    - Remover
        - Item: dic.pop("chave") ou dic.popitem()
        - Apaga tudo: dic.clear()
        - Chave: dic[chave]
    - Adiciona novas chaves - o valor pode ser vazio
        dic.fromkeys(["nome", "telefone"], valorChave) 
    
# urllib.request
    Biblioteca utilizada pra ler um site
        import urllib.request
        pagina = urllib.request.urlopen('http://beans.itcarlow.ie/prices-loyalty.html') -> abre a página
        texto = pagina.read().decode('utf8') -> lê a página html e inclui as tags html

# Time
    Biblioteca de tempo
    - Sleep: Para a execução do programa por um determinado tempo
        time.sleep(segundos)

# List Comprehension
    Forma compacta de montar uma lista, em apenas uma linha
    pares = [x for x in lista if x % 2 == 0]

# Print
    - Ao invés de pular uma linha ele cola os prints
        print('x', end = ' ')
        print('x', end = ' ')
        print('abacate', end = ' ')

# Ações de um repetidor: Break, Continue
    - Continue: Volta para o começo da repetição
        for k in range(10):
            if k % 2 == 0:
                continue
            print(k)
        (imprime apenas os impares, ignora os pares)
    - Break: Sai da repetição 

# Yield
    Retorno inteligente, separa o código em partes onde cada vez que é chamado retorna um dos yield, é inteligente pois reconhece a última chamada e onde parou.
        ex: No modo de escrita:
            def f():
            cont = 1
            fat = 1
            while True:
                yield fat
                cont += 1
                fat *= cont
        Modo interativo:
            x = f()
            next(x) - repete varias vezes e cada vez volta um valor

# Variáveis Global
    - global variavel
    ex: def fatec():
            global a
            a = 42
            print('dentro', a)
        fatec()
        print('depois', a)

# Tupla
    Uma lista imutavél, inclusive bloquia os elementos dentro dela. Defenida por parenteses e é uma boa prática colocar uma virgula no final para não confundir com operações. Funciona da mesma forma da array
        Ex: (1, 2, 3, 4,)

# Sets
    Coleção que não possui itens repetidos. Pode ser usado com qualquer coisa iterável. Não garante a ordem correta.
    Ex: repetida(1,2,3,3,1)
        set(repetida) -> {1,2,3}
    Não suporta indexação ou slicing - para acessar é necessário transformar em lista 
        list(set)
    Da pra usar repetições
    - Unir sets 
        setA.union(setB)
        Ex:
            conjunto_a = {1, 2}     conjunto_b = {3, 4}
            conjunto_a.union(conjunto_b) -> {1, 2, 3, 4}
    - Retornar a Interseccção de sets - elementos iguais entre si
        setA.intersection(setB)
    - Diferença de sets
        setA.difference(setB) -> elementos do A que são diferentes do B
        ou 
        setA.symmetric_difference(setB) -> elementos diferentes entre os dois
    - Subconjunto
      setA.issubset(setB) -> Retorna True ou Falso se A é subconjunto (está dentro) de B
    - Se todos elementos de um conjunto não está presente em outro
        setA.isdisjoint(setB) -> True ou False
    - Adicionar novo elemento 
        set.add(elemento)
    - Limpa um set
        set.clear()
    - Copiar um set
        set.copy()
    - Exclui um valor
        set.discard(elemento)
        ou 
        set.pop() -> apaga o primeiro valor
        ou 
        set.remove(elemento)
    - Tamanho de um set
        set.len()
    

# ------- PROGRAMAÇÃO ORIENTADA A OBJETOS ----------------------

# Classes
    Definida por:
        class nomeClasse:
    - Self: Atributo/variável que representa o objeto
    - Métodos: São as funções/ações de uma classe, obrigatoriamente recebe o self como primeiro argumento
        ex: def parar(sel):
        - Retornar a classe e seus atributos: Metódo automatizado para retornar o nome da classe de um obejto e seus atributos:
            def __str__(self):
                return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__items()])}"
            -> self.__class__.__name__ : Retorna o nome da classe
            -> self.__dict__ -> Retorna um dicionário com os atributos da classe e valores do objeto
            -> Utilização do list comprehension



## Construtor
    Método que sempre é executado quando uma nova instância da classe é criada. Onde é inicializado os atributos da classe
        def __init__(self):
            self.nome = nome        
    
## Destrutor
    Método que sempre é executado quando uma instância é excluida. Não é tão necessário em questões de salvar memória pois o Python já cuida disso, mas pode ser útil para realizar ações antes da exclusão
        def __del__(self):
            print("Destruindo a instância")
    O objeto já é destruída quando sua execução acaba, mas pode ser forçada através do comando:
        del nomeObjeto

## Herança
    Classes podem herdar comportamentos/atributos de outra classe. 
        class A: - Classe pai
        class B(A): - Classe filha, herda os comportamentos de A
    - Herança Simples: Classe filha herda de apenas uma classe pai 
    - Herança Múltipla: Classe filha herda de várias classes pais
        class C(A, B)
    - Para herdar o comportamento do pai:
        super()
        ex: super().__init__(self)
    - Ordem de execução das heranças: Para saber em que ordem as heranças estão sendo utilizadas
        classe.__mro__

## Encapsulamento
    Proteção de acesso, métodos públicos ou privados. No Python é apenas uma convenção, o interpretador não tem essa proteção.
        - Público: Pode ser acessado de fora da classe
        - Privado: Só pode ser acessado pela classe, o objeto não deveria ler nem alterar. Iniciado por underline -> _saldo

## Decoradores
    São convenções para tornar o código mais legível
    - Property: Basicamente permite que métodos sejam utilizados como atributos. Permite a modificação e retorno dinamico. Ex: Ao invés de criar um atributo idade cria-se:
        @property
        def idade(self):
            anoAtual = 2022
            return anoAtual - self.anoNascimetno
    Outro uso comum é para retornar o valor de um atributo:
        @property
        def anoNasc(self):
            return self.anoNasc
    - Setter: Para modificar o valor de um atributo
    @largura.setter:
    def largura(self, nova_largura):
        if nova_largura > 0:
            self._largura = nova_largura
        else:
            raise ValueError("A largura deve ser maior que 0.")



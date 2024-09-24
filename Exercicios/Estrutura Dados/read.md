# Estrutura de Dados
    Como saber se um algoritmo é bom ou ruim:
        - Nº de passos, espaço ocupado
        - tempo de execução

# Funções Recursivas
    Faz repetição no retorno do dado

    Estrutura:
        def funcaoRecursiva(arg):
            if caso mais simples return valor que sei
            else return devolve fórmula com diminuição de argumentos 
        
        Cada chamada da função gera uma instância

    Ex: 
    Teste de mesa:
        def pot(2, 3)

## Ponteiros
    As váriaveis são os ponteiros e aquilo que está armazenado são os objetos.
        x = 45; x - ponteiro 45 - obj
    Se há dois ponteiros apontando para mesmo objeto, quando o objeto é alterado muda para os dois ponteiros. 
        Ex: x = 45   |   x = 20
            y = x    |   então, y também é igual a 20
    Para mudar isso, é necessário copiar ponteiros através de métodos contrutores, que constroi um novo objeto igual ao outro
        Ex: x = 45                                                |   x = 20
            y = list(x) # list é o método construtor de listas    |   então, y também é igual a 20

    *x = aponta para a posicao da memoria, nn muda o endereço
    x = cria um novo endereço, 

    int *p = estou declarando, apontando pra uma posicao
    *p = estou acessando o local 

    Se usam ponteiros para:
        > Acessar variáveis fora do escopo local
        > Fazer vetores com alocação dinâmica

## Lista Encadeada/Ligada
    Utilizam-se ponteiros, nenhum item mudará de vetor, apenas o ponteiro irá mudar de endereço.

    A cabeça serve para evitar ponteiros que apontar pra ponteiros (**p) e precisar perguntar se a lista está vazia (pois em sua maioria a lista não vai esta vazia).

    Para retornar um valor é necessário retornar o conteudo de um ponteiro: p->conteudo

    Para liberar toda uma lista encateada para a memoria (usa-se o free(ponteiro)), é necessário percorrer a lista e ir dando o free porém salvar o endereço do ponteiro a ser liberado antes para que ainda haja a ligação com o resto da lista (possivel usar o p->seg)


# Busca binária
    Algoritmo de busca basicamente vai dividindo a lista e verificando em qual pedaço a lista está através da verificação de qual é menor

    - Algoritmos de sort:
        
        - Inserção ('Algoritmo do baralho'): Consiste em percorrer a lista da esqueda pra direita e vai ordenando /** algoritmo ruim
        Ex:  4 5 2 0 3 7 6 1
        4 5 2 0 3 7 6 1 -> 4 é o primeiro, já está em ordem
        4 5 -> 5 é maior que 4, não mexe
        2 4 5 -> 2 é menor que 5, empurra o 5, 2 menor que o 4, empurra o 4
        0 2 4 5 -> 0 empurrou 245
        0 2 3 4 5 -> 3 empurrou 45
        0 2 3 4 5 6 7 -> 6 empurrou o 7
        0 1 2 3 4 5 6 7 -> 1 empurrou 2437

        Total de passos = n * n 

        7 5 0 1 2 3 6 4
        7 5 0 1 2 3 6 4
        5 7 -> 7 empurrou o 5
        0 5 7 -> 0 empurro o 57
        0 1 5 7 -> 1 empurrou o 57 
        0 1 2 5 7 -> 2 empurrou o 57
        0 1 2 3 5 7 -> 3 empurrou o 57
        0 
        
    - Seleção: Percorre todo mundo da esquerda para direita e busca o menor de todos (min) à direita da atual e troco o atual com o menor de todos (min) /* algoritmo ruim pq sempre percorre tudo
        Ex: 7 5 0 1 2 3 6 4 
        5 7 0 1 2 3 6 4 -> Troca o 5 por 0 (percorre tudo à direita -> 7012364)
        0 5 7 1 2 3 6 4 -> Troca 1 com 5
        0 1 7 5 2 3 6 4 -> Troca 2 com 7 
        0 1 2 5 7 3 6 4 -> Troca 5 com 3
        0 1 2 3 7 5 6 4 -> Troca 7 com 4 
        0 1 2 3 4 5 6 7 -> Troca 6 com 6
        0 1 2 3 4 5 6 7 -> Troca 7 com 7

    - Mergesort: Divide o vetor em dois até chegar em vetores de 1 elemento, depois junta de novo porém comparando; /* bom pq é rapido, mas usa o dobro da memória
        7 5 0 1 2 3 6 4 
        7501 2364
        75 01 23 64
        7 5 0 1 2 3 6 4
        57 01 23 46
        0157 2346 -> faz chuvinha p achar (5 compra com 0 1; )
        0 1 2 3 4 5 6 7

        para melhorar, teriamos que fazer um processamento paralelo, processando duas metades de uma vez pois uma não interfere na outra

    - Quicksort: Escolhe-se um voluntrário (pivô) e dividir o mundo em menores e maiores que o voluntário. O voluntário sempre ficará na posição final do vetor, e a cada divisão dobra-se a quantidade de voluntários, ou seja, o número de passos seria log(n,2). Usa-se a recursão para fazer a divisão várias vezes até chegar ao final. /* muito bom, o pior caso é quando o vetor já está em ordem (então vou gastar n passos e n passos para se compararem com o voluntário - n * n) mas isso é muito raro */
        2 0 5 7 3 1 6 4 
        0 1 2 5 7 3 6 4
        0 1   3 4 5 7 6
              3 4   6 7

    - Heapsort (nn cai na prova): Ele divide os indices do vetor





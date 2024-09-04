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




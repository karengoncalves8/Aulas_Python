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

# C e C++

    *x = aponta para a posicao da memoria, nn muda o endereço
    x = cria um novo endereço, 

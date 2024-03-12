# Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles usando 
# o algoritmo de Euclides. 

n1 = int(input('Digite um número: '))
n2 = int(input('Digite mais um número: '))

while n1 != 0 and n2 != 0:
    n1, n2 = n2, n1 % n2

print(f'O MDC de ({n1}, {n2}) é {n1}')
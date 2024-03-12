# Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um 
# terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
# intercalados dos dois outros vetores. Imprima os três vetores.

import random

lista1 = []
lista2 = []
lista3 = []

for k in range(10):
    x = random.randint(1, 100)
    lista1.append(x)
    lista3.append(x)
    y = random.randint(1, 100)
    lista2.append(y)
    lista3.append(y)

print(f'''Lista: {lista1}
Pares: {lista2}
Impares: {lista3}''')
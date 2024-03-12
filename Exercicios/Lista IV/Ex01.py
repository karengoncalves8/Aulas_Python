# Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar 
# as funções max e min.

import random

lista = random.sample(range(100), 10)

min = 0
max = 101

for n in lista:
    if n < max: 
        max = n
    if n > min:
        min = n

print(f'Na lista {lista} o maior número é {max} e o menor {min}')
    
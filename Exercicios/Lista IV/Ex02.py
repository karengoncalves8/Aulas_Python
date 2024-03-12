# Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os 
# números ímpares na lista IMPAR. Imprima as três listas.

import random 

lista = random.sample(range(100), 20)
pares = []
impares = []

for n in lista:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print(f'''Lista: {lista}
Pares: {pares}
Impares: {impares}''')
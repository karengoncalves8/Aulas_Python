# import random

# nomes = ['bianca', 'karen', 'sarah']

# print(random.choice(nomes))

####### Mês por extenso
meses = 'janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'.split()

d, m, a = input('data (dd-mm-aaaa): ').split('-')

print(d, 'de', meses[int(m) - 1], 'de', a)

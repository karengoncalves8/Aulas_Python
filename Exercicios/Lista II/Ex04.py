# Faça um Programa que leia três números e mostre o maior deles.

print(f'{'='*5} Maior Número {'='*5}')

a = int(input("Informe um valor: "))
b = int(input("Informe mais um valor: "))
c = int(input("Informe mais um valor: "))

if (b < a > c) or (b == a > c) or (c == a > b):
    print(f'O maior número é {a}')
elif (a < b > c) or (a == b > c) or (b == c > a):
    print(f'O maior número é {b}')
elif (b < c > a) or (a == c > b) or (b == c > a): 
    print(f'O maior número é {c}')
else:
    print('Os números são iguais')



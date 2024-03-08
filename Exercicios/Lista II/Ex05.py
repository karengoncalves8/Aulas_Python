# Faça um Programa que leia três números e mostre o maior e o menor deles

print(f'{'='*5} Menor Número {'='*5}')

a = int(input("Informe um valor: "))
b = int(input("Informe mais um valor: "))
c = int(input("Informe mais um valor: "))

if (b > a < c) or (b == a < c) or (c == a < b):
    print(f'O menor número é {a}')
elif (a > b < c) or (a == b < c) or (c == b < a):
    print(f'O menor número é {b}')
elif (a > c < b) or (a == c < b) or (b == c < a):
    print(f'O menor número é {c}')
else:
    print('Os números são iguais')
# Faça um Programa que leia três números e mostre o maior e o menor deles

print(f'{'='*5} Menor Número {'='*5}')

n1 = int(input("Informe um valor: "))
n2 = int(input("Informe mais um valor: "))
n3 = int(input("Informe mais um valor: "))

if n2 < n1 > n3:
    ma = n1
    if n2 < n3: 
        me = n2
    else:
        me = n3
elif n1 < n2 > n3:
    ma = n2
    if n1 < n3: 
        me = n1
    else:
        me = n3
elif n1 < n3 > n2:
    ma = n3
    if n1 < n2: 
        me = n1
    else:
        me = n2

print(ma,me)
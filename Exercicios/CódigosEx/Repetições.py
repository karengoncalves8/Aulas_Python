###### Número Par
# n = int(input("Digite um número: "))
# x = 0

# while x <= n:
#     if x % 2 == 0:
#         print(x)
#     x += 1

###### Número Impar
# n = int(input("Digite um número: "))
# x = 0

# while x <= n:
#     if x % 2 != 0:
#         print(x)
#     x += 1

###### Múltiplos de 3
# n = int(input("Digite um número: "))
# x = 0
# while x < 10:
#     if n % 3 == 0:
#         print(n)
#         x += 1
#     n += 1

###### Soma de três números (acumulador)
# x = 1
# soma = 0
# while x <= 3:
#     n = int(input('Digite um número: '))
#     soma = soma + n
#     x = x + 1
# print(soma)

###### Média de três números
# x = 1
# soma = 0
# while x <= 3:
#     n = int(input('Digite um número: '))
#     soma = soma + n
#     x = x + 1
# print(soma/3)

##### Fatorial de um número
# x = 1
# fat = 1
# n = int(input('Digite um número: '))

# while x <= n:
#     fat = fat * x
#     x = x + 1

# print(fat)

##### Interrompendo a repetição
soma = 0
while True:
    x = int(input('n (zero sai): '))
    if x == 0:
        break
    soma = soma + x
    print(f'Soma: {soma}')



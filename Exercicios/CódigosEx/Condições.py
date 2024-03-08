###### Exercicio Slide - Velocidade

# v = int(input("Informe a velocidade do carro (km/h): "))

# if v > 110:
#     m = (v - 110)*5
#     print(f"Você foi multado! O valor a ser pago é de R${m}")
# else:
#     print("Tudo certo.")


###### Exercicio Slide - Maior Número 

# a = int(input("Primeiro valor: "))
# b = int(input("Segundo valor: "))
# c = int(input("Terceiro valor: "))

# if a > b and a > c:
#     if b > c:
#         print(f'A sequência em ordem decrescente é {a, b, c}')
#     if c > b:
#         print(f'A sequência em ordem decrescente é {a, c, b}')
# if b > a and b > c:
#     if a > c:
#         print(f'A sequência em ordem decrescente é {b, a, c}')
#     if c > a:
#         print(f'A sequência em ordem decrescente é {a, c, a}')
# if c > a and c > b:
#     if a > b:
#         print(f'A sequência em ordem decrescente é {c, a, b}')
#     if b > a:
#         print(f'A sequência em ordem decrescente é {c, b, a}')


###### Exercicio Slide - Idade do Carro
# idade = int(input("Digite a idade de seu carro: "))

# if idade <= 3:
#     print("Seu carro é novo")
# else:
#     print("Seu carro é velho")

###### Exercicio Slide - Estrutura aninhadas
min = int(input("Informe a quantidade de minutos: "))

if min < 200:
    valor = min * 0.20
elif min <= 400:
    valor = min * 0.18
elif min <= 800:
    valor = min * 0.15
else:
    valor = min * 0.08
    
print(f'O preço da sua conta de telefone é R${valor:.0f}')
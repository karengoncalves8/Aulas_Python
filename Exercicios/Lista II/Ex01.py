# Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser 
# um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

print(f'{'='*5} Verificação de Triângulo {'='*5}')
l1 = int(input("Informe um dos lados do triângulo: "))
l2 = int(input("Informe um dos lados do triângulo: "))
l3 = int(input("Informe um dos lados do triângulo: "))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
     if l1 ==  l2 == l3:
          print('Os valores informados pode ser um triângulo equilátero')
     elif (l1 == l2 != l3) or (l2 == l3 != l1) or (l3 == l1 != l2):
          print('Os valores informados pode ser um triângulo isósceles')
     else:
          print('Os valores informados pode ser um triângulo escaleno')
else:
     print('Os valores informados não pode ser um triângulo')
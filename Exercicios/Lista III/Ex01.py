# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido.

n = int(input('Dê uma nota de 0 à 10: '))

while 10 < n > 0:
    n = int(input('Dê uma nota de 0 à 10: '))

    

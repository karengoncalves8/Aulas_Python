# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de 
# seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do 
# estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
# faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na 
# variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais 
# variáveis com o conteúdo ZERO.

print(f'{'='*5} Rendimento Diário {'='*5}')

peixes = int(input('Informe a quantidade pescada hoje (kg): ')) 

if peixes > 50:
    ex = peixes - 50
    print(f'Você excedeu o peso em {ex}kg e deverá pagar uma multa de R${ex*4}')
else:
    print(f'Tudo certo! Você não excedeu o peso.')
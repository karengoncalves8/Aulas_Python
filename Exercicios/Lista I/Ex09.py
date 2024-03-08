# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo 
# usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

print("="*5, "Aluguel de Carro", "="*5)

km = float(input("Digite a quantidade de km percorridos: "))
d = int(input("Digite a quantidade de dias: "))

print(f'O preço a ser pago será de R${(km*0.15 + 60*d):.0f}')
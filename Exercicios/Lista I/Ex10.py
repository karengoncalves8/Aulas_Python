# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a 
# quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante 
# perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o 
# total de dias.

print("="*5, "Redução do tempo de vida de um fumante", "="*5)

qt = int(input("Informe a quantidade de cigarros fumados por dia: "))
an = int(input("Informa a quantidade de anos fumados: "))

dp = (qt*an)*10

print(f'O tempo de vida perdido devido ao fumo será de {dp:.0f} dias')
# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a 
# ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida
# em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem 
# compradas e o preço total. Obs. : somente são vendidos um número inteiro de latas

print(f'{'='*5} Loja de Tintas {'='*5}')
m2 = int(input('Informe a área a ser pintada (m2): '))

l = m2/3
if l % 18 != 0:
    qtLatas = int((l/18) + 1)
else:
    qtLatas = l/18

p = qtLatas * 80

print(f'No total serão {qtLatas:.0f} latas, que irão custar R${p:.0f}')
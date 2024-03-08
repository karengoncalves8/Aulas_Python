# Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. 
# Calcule o total em segundos.

print("="*5, "Total em Segundos", "="*5)
print("Digite a quantidade de:")
d = int(input("Dias: "))
h = int(input("Horas: "))
m = int(input("Minutos: "))
s = int(input("Segundos: "))

print("O total em segundos é:", (d*86400) + (h*3600) + (m*60) + s)

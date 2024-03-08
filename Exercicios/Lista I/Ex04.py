# Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento. 
# Exiba o valor do aumento e do novo salário.

print("="*5, "Reajuste de Salário", "="*5)
sal = float(input("Digite o valor de seu salário: "))
porc = int(input("Digite a porcentagem de aumento: "))

salAumento = sal*(porc/100)

print("Você recebeu um aumento de R$", salAumento, "e seu salário agora é de R$", sal+salAumento)

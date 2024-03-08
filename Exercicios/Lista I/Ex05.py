# Solicite o preço de uma mercadoria e o percentual de desconto. 
# Exiba o valor do desconto e o preço a pagar.

print("="*5, "Desconto em uma mercadoria", "="*5)

v = float(input("Informe o valor da mercadoria: "))
porc = int(input("Informe o percentual de desconto: "))

desc = v*(porc/100)

print("Você recebeu um desconto de R$", desc, "e irá pagar R$", v-desc)
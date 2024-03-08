# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule 
# e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS, 
# quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os 
# descontos e o salário líquido, conforme a tabela abaixo:

print(f'{'='*5} Rendimento do mês {'='*5}')

salHora = float(input("Informe a quantidade de ganho por hora: "))
horasT = int(input("Informe a quantidade de horas trabalhadas no mês: "))

salB = salHora * horasT
ir = salB * 0.11
inss = salB * 0.08
sind = salB * 0.05
salLiq = salB - ir - inss - sind

print(f'''
    Salário Bruto: {salB:.0f}
    Foi pago ao INSS: {inss:.0f}
    e ao Sindicato: {sind:.0f}
    Salário Líquido: {salLiq:.0f}
      ''')


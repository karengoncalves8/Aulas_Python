# Mostrar os fornecedores em ordem do valor que mais receberam da cota parlamentar, em ordem decrescente, use um dicionário para guardar todos os valores. Dica: lembre que existe o sorted(dicionário, key=função, ...) onde a função irá devolver o valor para um determinado item do dicionário.
# Ex.: Mostrar os maiores fornecedores que receberam verbas da deputada Tabata do Amaral em 2023

import requests

gastos = {}
 
for p in range(1, 100):
    URL = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2023&ordem=ASC&ordenarPor=ano&pagina={p}&itens=15'

    resp = requests.get(URL).json()

    for x in resp['dados']:
        fornecedor = x['nomeFornecedor']
        if fornecedor not in gastos:
            gastos.setdefault(fornecedor, x['valorLiquido'])
        else:
            gastos[fornecedor] += x['valorLiquido']

gastos = sorted(gastos.items(), key=lambda item:item[1], reverse=True)

print(gastos)                                                 
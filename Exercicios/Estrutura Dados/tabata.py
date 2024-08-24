import requests

total = 0
 
for p in range(1, 46):
    URL = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ordem=ASC&ordenarPor=ano&pagina={p}&itens=15'
    print(f'pagina: {p}')

    resp = requests.get(URL).json()

    for x in resp['dados']:
        total = total + x['valorLiquido']

print(f'R$ Total = {total:.2f}')


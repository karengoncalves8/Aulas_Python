import requests

valor = 0
cnpj = {}
fornecedores = {}
 
for p in range(1, 46):
    URL = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/despesas?ano=2023&ordem=ASC&ordenarPor=ano&pagina={p}&itens=15'

    dados = requests.get(URL).json()['dados']

    for d in dados:
        c = d['cnpjCpfFornecedor']
        n = d['nomeFornecedor']
        if c not in cnpj:
            cnpj[c] = d['valorLiquido']
            fornecedores[c] = n
        else:
            cnpj[c] += d['valorLiquido']
        
        valor += d['valorLiquido']

print(cnpj)
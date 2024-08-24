import requests

URL = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
 
dados = requests.get(URL).json()
 
r = ''
 
for i in dados['dados']:
    if i['siglaPartido'] == 'PSOL' and i['siglaUf'] == 'SP':
        print(i['nome'])
        r = requests.get(i['urlFoto'], allow_redirects=True)
 
        open('Fotos/' + i['nome'] + '.png', 'wb').write(r.content)


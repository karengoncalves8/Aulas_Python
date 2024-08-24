import requests
#nltk.download("stopwords")                                                                                                                                                                                                                                                                                   
from nltk.corpus import stopwords
import string

palavras = []
 
for p in range(1, 8):
    URL = f'https://dadosabertos.camara.leg.br/api/v2/deputados/204534/discursos?dataInicio=2019-01-01&dataFim=2024-08-14&ordenarPor=dataHoraInicio&ordem=ASC&pagina={p}&itens=15'

    resp = requests.get(URL).json()

    for x in resp['dados']:
        stop_words = set(stopwords.words('portuguese'))
        texto = x['transcricao'].lower()
        
        
        for word in x['transcricao']:
            print(word)
            if word not in stop_words:
                palavras.append(word)

# print(f'palavras: {palavras}')
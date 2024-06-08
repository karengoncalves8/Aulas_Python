# Nos 3 casos abaixo mostre os alunos em ordem decrescente de nota, irá notar que a última é bem difícil. 
# Dicas: use items(), values() para os dicionários.
# alunos1 = {7:'pedro', 9:'maria', 8:'luiz'}
# alunos2 = {'pedro': 7, 'maria':9, 'luiz':8}
# alunos3 = [{'pedro': 7}, {'maria':9}, {'luiz':8}]

alunos1 = {7:'pedro', 9:'maria', 8:'luiz'}
print(sorted(alunos1.items(), reverse=True))
 
alunos2 = {'pedro': 7, 'maria':9, 'luiz':8}
print(sorted(alunos2.items(), key= lambda item: item[1], reverse=True))

alunos3 = [{'pedro': 7}, {'maria':9}, {'luiz':8}]
print(sorted(alunos3, key = lambda item : tuple(item.values()), reverse=True))
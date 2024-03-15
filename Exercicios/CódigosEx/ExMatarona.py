# Leia um número inteiro positivo. Se o numeru divisivel por 3 mostre a saída 'fizz',
# se ele é divisível por 5 mostre a saída 'buzz', porém se ele e divisivel ao mesmo tempo por 3 
# e por 5 mostre a saida 'fizzbuzz'. Passando por todas as regras anteriores, se ele é divisivel por 
# 42 (regra máxima e prioritária), mostre a saída 'resposta para tudo'. Se o número não se enquadrar 
# em nenhuma das regras anteriores, mostre apenas o número lido na saída


n = int(input('Digite um número:' ))

if(n % 42 == 0 ):
    print('Resposta para tudo')
elif(n % 3 == 0 and n % 5 == 0):
    print('fizzbuzz')
elif(n % 3 == 0):
    print('fizz')
elif(n % 5 == 0):
    print('buzz')
else: 
    print(n)

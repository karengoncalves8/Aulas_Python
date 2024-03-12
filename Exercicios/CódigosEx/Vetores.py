# predio = ['zelador', 'familia silva', 'sr henrique', 'familia souza']
# predio.append('luciola')

# print(predio)

# texto = "Batatinha quando nasce esparrama pelo chão, menina quando dorme, põe a mão no coração"

# texto = texto.split(", ")

# print(texto)

#### Ex 4
texto = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you'''
texto = texto.replace('.',' ')
texto = texto.replace(':',' ')
texto = texto.replace(',',' ')
texto = texto.lower()
texto = texto.split()

# lista = []
# for p in texto:
#     if p[0] in 'python' or p [-1] in 'python':
#         lista.append(p)

# print(lista)


# Achar uma letra específica 
for p in texto:
    for letra in p:
        if letra == 'x':
            print('achou', p)
# Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras 
# “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para 
# minúsculas e de remover antes os caracteres especiais

texto = '''The Python Software Foundation and the global Python 
community welcome and encourage participation by everyone. Our community is based on 
mutual respect, tolerance, and encouragement, and we are working to help each other live up 
to these principles. We want our community to be more diverse: whoever you are, and 
whatever your background, we welcome you.'''

texto = texto.replace('.', ' ')
texto = texto.replace(',', ' ')
texto = texto.replace(':', ' ')
texto = texto.lower()
texto = texto.split()
count = 0

for x in texto:
    if len(x) > 4:
        for y in x:
            if y in 'python':
                count += 1
                break

print(count)

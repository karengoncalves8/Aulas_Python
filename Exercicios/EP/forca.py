# Karen Gonçalves

import urllib.request
import random 

palavras_site = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt') 
texto = palavras_site.read().decode('utf8') 
texto = texto.split()   

forca = ['''
    +-----------+
    |           |
                |
                |                      
                |
                |
                |           
==================
      ''',
      '''
    +-----------+
    |           |
    O           |
                |                      
                |
                |
                |           
==================
      '''
    , 
     '''
    +-----------+
    |           |
    O           |
    |           |                      
                |
                |
                |           
==================
      '''
    ,
'''
    +-----------+
    |           |
    O           |
    |\\          |                      
                |
                |
                |           
==================
      '''
    ,
'''
    +-----------+
    |           |
    O           |
   /|\\          |                      
                |
                |
                |           
==================
      '''
    ,
'''
    +-----------+
    |           |
    O           |
   /|\\          |                      
   /            |
                |
                |           
==================
      '''
    ,
      '''
    +-----------+
    |           |
    O           |
   /|\\          |                      
   / \\          |
                |
                |           
==================
      ''']

# Forca 0 a 6

print(f'{'='*10} Jogo da Forca {'='*10}')

def escolhe():
    return random.choice(texto)

def chute(letra):
    if letra.isalpha():
        if letra not in certas or letra not in erradas:
            return letra
        else:
            print('Letra já tentada')
            return False
    print('Caractere inválido')
    return False

def jogar_novamente(res):
    return res.lower() == 's'
    
def ganhou():
    if len(palavra) == len(certas):
        for l in certas:
            if l not in palavra:
                return False
        return True
    return False

def desenha():
    print(forca[len(erradas)])
    for x in palavra: 
        if x in certas:
            print(x, end=' ')
        else:
            print('_', end=' ')

certas = ''
erradas = ''
palavra = ''

while True:
    if not palavra:
        palavra = escolhe()
    desenha()
    letra = str(input('Chute uma letra: '))
    if chute(letra):
        if letra in palavra:
            certas += letra
        else:
            erradas += letra
        if ganhou():
            print(f'Parabéns! Você acertou a palavra {palavra}')
            res = str(input('Deseja jogar novamente? [S/N]'))
            if jogar_novamente:
                certas = ''
                erradas = ''
                palavra = ''
                continue
            else:
                False
        if len(erradas) >= 6:
            print('Você perdeu!')
    else:
        continue

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
        if letra not in certas and letra not in erradas:
            return True
        else:
            print('Letra já tentada')
            return False
    print('Caractere inválido')
    return False

def jogar_novamente(res):
    return res.lower() == 's'
    
def ganhou():
    for l in palavra:
        if l not in certas:
            return False
    return True

def desenha():
    print(forca[len(erradas)])
    for x in palavra: 
        if x in certas:
            print(x, end=' ')
        else:
            print('_', end=' ')

certas = ''
erradas = ''
palavra = escolhe()

while True:
    desenha()
    if len(erradas) == 6:
        print(f'\nVocê perdeu! a palavra era {palavra}')
        res = str(input('\nDeseja jogar novamente? [S/N] '))
        if jogar_novamente(res):
            certas = ''
            erradas = ''
            palavra = escolhe()
            continue
        else:
            break
    letra = str(input('\n\nChute uma letra: '))
    if chute(letra):
        if letra in palavra:
            certas += letra
        else:
            erradas += letra
        if ganhou():
            print(f'\nParabéns! Você acertou a palavra {palavra}')
            res = str(input('\nDeseja jogar novamente? [S/N] '))
            if jogar_novamente(res):
                certas = ''
                erradas = ''
                palavra = escolhe()
                continue
            else:
                break

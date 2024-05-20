# D. Dada uma lista de números retorna uma lista sem os elementos repetidos
# PS: se você usar o comando set deve ficar ordenado
# como aparece no resultado dos testes
def remove_iguais(nums):
  return sorted(set(nums))

# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar
def cripto(frase):
  frase = frase.split()
  nv_frase = []
  for p in frase:
    nv = sorted(set(p))
    nv = ''.join(nv)
    nv_frase.append(nv)
  return ' '.join(nv_frase)


# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2
def derivada(coef):
  lista = []
  pot = 2
  for n in coef[2:]:
    lista.append(n * pot)
    pot += 1
  lista.insert(0, coef[1])
  return lista


# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# pode supor que n1 e n2 tem o mesmo número de dígitos
# Não vale converter a lista em número para somar diretamente
def soma(n1, n2):
  lista = []
  v1 = 0
  for x, y in zip(n1, n2):
    n = (x + y) % 10 + v1
    v1 = (x + y) // 10
    lista.append(n)
  if v1 != 0: 
    lista.append(v1)
  return lista

# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é, uma palavra é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  return sorted(s1) == sorted(s2)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('remove_iguais')
  test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
  test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
  test(remove_iguais([]), [])

  print ()
  print ('cripto')
  test(cripto('ana e mariana gostam de banana'),
       'an e aimnr agmost de abn')
  test(cripto('Batatinha quando nasce esparrama pelo chão'),
       'Bahint adnoqu acens aemprs elop choã')

  print ()
  print ('derivada de polinômio')
  test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
  test(derivada([4, 16, 1]), [16, 2])

  print ()
  print ('soma em listas invertidas')
  test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1]) # [4, 3, 2, 5] + [8, 7, 8, 9]
  test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])

  print ()
  print ('anagrama')
  test(anagrama('abacate', 'abacatx'), False)
  test(anagrama('sim', 'xxs'), False)
  test(anagrama('sim', 'siiimmmmm'), False)
  test(anagrama('iracema', 'america'), True)
  test(anagrama('ator', 'rota'), True)
  test(anagrama('aberto', 'rebato'), True)
  test(anagrama('amor', 'roma'), True)
  test(anagrama('ramo', 'amor'), True)
  test(anagrama('baba', 'aba'), False)
  test(anagrama('casa', 'cassa'), False)
  test(anagrama('palmeiras', 'abacate'), False)
  test(anagrama('alegria', 'alergia'), True)
  test(anagrama('cantiga', 'catinga'), True)

if __name__ == '__main__':
  main()

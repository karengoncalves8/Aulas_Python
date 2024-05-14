# Given two positive integers n and k, generate all binary integer between 0 and 2 ** n-1, inclusive. 
# These binaries will be drawn in descending order according to the number of existing 1s. 
# If there is a tie choose the lowest numerical value. Return the k-th element from the selected list.
# Eg n = 3 and k = 5
# ['0 b111 ', '0 b11', '0 B101 ', 
# '0 b110', '0 b1 ', '0 b10', '0 b100 ', '0 b0']
# fifth element '0 b1 '
def count_one(b):
    return b.count('1')

def binary(n, k):
    list = []
    for i in range(2**n):
       list.append(bin(i))
    list = sorted(list, key=count_one, reverse=True)
    return list[k-1]

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))
  
test(binary(3, 5), '0b1')



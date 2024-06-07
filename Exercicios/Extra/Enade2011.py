# 1 2 4 8 
# 1 3 7 15 
# 1 2 3 4

# graos = 0
# an = 1
# for i in range(1, 4):
#     graos += an * 2
#     an = graos 

# print(graos)

def Josephus(n, m):
    circulo = [p for p in range(1, n+1)]
    while circulo != 1:
        for p in range(0, len(circulo), m):
            circulo.remove(circulo[p])

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))
  
test(Josephus(50, 3), 11)


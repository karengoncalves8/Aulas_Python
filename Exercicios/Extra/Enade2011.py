# 1 2 4 8 
# 1 3 7 15 
# 1 2 3 4

graos = 0
an = 1
for i in range(1, 4):
    graos += an * 2
    an = graos 

print(graos)
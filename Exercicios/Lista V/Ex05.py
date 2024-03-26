#  Na pacata vila campestre de Ponteironuloville, todos os telefones têm 6
# dígitos. A companhia telefônica estabelece as seguintes regras sobre os números:
# 1. Não pode haver dois dígitos consecutivos idênticos, porque isso é chato;
# 2. A soma dos dígitos tem que ser par, porque isso é legal;
# 3. O último dígito não pode ser igual ao primeiro, porque isso dá azar

numeros = '''100 220 202 1032 000'''
count = 0
numeros = numeros.split()

for n in numeros:
    n1 = 0
    soma = 0
    for x in n:
        if n1 == x: 
            break
        n1 = x
        soma += int(x)
    if soma != 0 and soma % 2 == 0:
        count += 1

print(count)


# soma
# for n in numeros:
#     soma = 0
#     for x in n:
#         x = int(x)
#         soma += x
#     if soma % 2 == 0:
#         count += 1
        
# comeco e fim
# for n in numeros:
#     if n[0] == n[-1]:
#         print(n)
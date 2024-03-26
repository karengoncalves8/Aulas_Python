# Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo 
# se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números 
# sortudos existem entre 18644 e 33087, incluindo os extremos?

count = 0
for i in range(18643, 33087):
    i = str(i)
    if '2' in i and '7' not in i:
        count += 1

print(count)

# Resposta: 7995
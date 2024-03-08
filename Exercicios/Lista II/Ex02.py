#  Determine se um ano é bissexto. Verifique no Google como fazer isso.

print(f'{'='*5} Ano Bissexto {'='*5}')

ano = int(input('Informe um ano: '))

if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
        print('É bissexto')
else:
    print('Não é bissexto')
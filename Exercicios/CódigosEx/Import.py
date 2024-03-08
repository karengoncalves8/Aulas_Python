# import calendar
# print(calendar.isleap(2024))

# is leap verifica se o ano é bissexto
# help (calendar.isleap) mostra como usa a função e pra que serve

year = int(input('Ano: '))

if year % 4 == 0 and \
    (year % 100 != 0 or year % 400 == 0):
        print('É bissexto')
else:
    print('Não é bissexto')

# if m % 54 == 0:
#       latas = m / 54
# else: 
#       latas = int(m /54) + 1

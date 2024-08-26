# Função para inverter palavra -> inv('abacate') -> 'etacaba'
# def inv(s):
#     if s == '': return s
#     return s[-1] + inv(s[:-1])

# print(inv('abacate'))

# Somar os algorismos -> sd(123) -> 1, 2, 3 = 6
# def sd(n):
#     str(n)
#     if n == '': return 0
#     return int(str(n)[-1]) + int(sd(str(n)[:-1]))
# print(sd(123))

# Sequencia de Fibonacci F1 - 1, F2 - 1, F3 - 2, F4 - 3, F5- 5
# def fib(n):
#     if n == 1 or n == 2: return 1
#     return fib(n-2) + fib(n-1)

# print(fib(3))

# MDC Euler -> mdc(21, 15) -> 3 
# def mdc(n1, n2):
#     if n2 == 0: return n1
#     return mdc(n2, n1 % n2)

# print(mdc(21, 15))

# numero para binario -> dec2bin(18) -> '10010' pesquisar como tranformar 
def dec2bin(n):
    n = int(n)
    if n < 2: return n % 2
    return str(dec2bin(n/2)) + str(n % 2)

print(dec2bin(18))

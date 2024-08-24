# def fat(n):
#     if n <= 1: return 1
#     return n* fat(n-1)

# print(fat(3))

# def pot(x, y):
#     if y == 0: return 1
#     return x * pot(x, y-1)

# print(pot(2,3))

# dic = {}
# def fib(n):
#     if n == 1 or n == 2: return 1
#     if n not in dic: dic[n] = fib(n-1) + fib(n-2) # Memorização, está guardando os cálculos que já foram realizados
#     return dic[n]

# print(fib(100))


# Usar o cache, o próprio sistema operacional ignora chamadas repetidas
# from functools import lru_cache

# @lru_cache(maxsize = None)
# def fib(n):
#     if n == 1 or n == 2: return 1
#     return fib(n-1) + fib(n-2)
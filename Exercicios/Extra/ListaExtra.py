def pi(n):
    den = 3
    pi = 4
    for i in range(1, n):
        if i % 2 != 0:
            pi -= 4/den 
        else:
            pi += 4/den 
        den += 2
    return pi

print(pi(1000))

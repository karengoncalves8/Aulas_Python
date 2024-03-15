def pythonica(palavra):
    if len(palavra) > 4:
        for x in palavra:
            if x in 'python':
                return True
    return False

print(pythonica('abc'))
# Função para inverter palavra -> inv('abacate') -> 'etacaba'

def inv(s):
    if s == '': return s[-1]
    return s + s[len(s)-1]

print(inv('abacate'))
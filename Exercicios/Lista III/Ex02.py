# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao 
# nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nomeU = str(input('Digite seu nome de usuário: '))
senha = str(input('Digite uma senha: '))

while nomeU == senha:
    print('ERRO! Sua senha não deve ser a mesma que seu nome de usuário.')
    nomeU = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite uma senha: '))

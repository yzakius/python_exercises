'''
nome = input('Qual o seu nome? ')
print('Tudo maiúsculo: {}'.format(nome.upper()))
print('Tudo minúsculo: {}'.format(nome.lower()))
lista = nome.split()
print('O nome completo possui {} letras'.format(len(''.join(lista))))
print('O seu primeiro nome é {} e possui {} letras'.format(lista[0], len(lista[0])))
'''

# Solução do professor

nome = str(input('Qual o seu nome? ')).strip()
print('Tudo maiúsculo: {}'.format(nome.upper()))
print('Tudo minúsculo: {}'.format(nome.lower()))
print('O nome completo possui {} letras'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome possui {} letras'.format(nome.find(' ')))

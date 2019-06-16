'''
Desafio 027 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.

# Minha Solução
nome = str(input('Olá. Qual o seu nome completo? ')).strip()
print('Olá {}'.format(nome))
n1 = nome.split()
n2 = n1[::-1]
print('O seu primeiro nome é {}.'.format(n1[0]))
print('O seu último nome é {}'.format(n2[0]))
'''

# Solução do professor
nome = str(input('Olá. Qual o seu nome completo? ')).strip()
print('Olá {}'.format(nome))
n1 = nome.split()
print('O seu primeiro nome é {}.'.format(n1[0]))
print('O seu último nome é {}'.format(n1[len(n1) - 1]))


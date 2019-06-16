'''
Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Digite um nome: ')).strip()

print('Tem Silva no nome?: {}'.format('SILVA' in nome.upper()))


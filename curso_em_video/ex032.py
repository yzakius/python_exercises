'''
Escreva um programa que leia qualquer e mostre se ele é bissexto.

# MINHA SOLUCAO

ano = int(input('Digite um ano:' ))

if ano % 4 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))
'''
from datetime import date
# Solução do Professor


ano = int(input('Digite um ano ou digite 0 para o ano atual  '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano Bissexto'.format(ano))
else:
    print('{} não é Bissexto'.format(ano))

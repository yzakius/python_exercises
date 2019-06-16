'''
@python **Desafio 028:** escreva um programa que faça o computador pensar qem um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu.
'''

from random import randint
from time import sleep

print('~' * 40)
print('Estou pensando em número entre 0 e 5.')
print('Você consegue adivinhar?')
print('~' * 40)
print('')
print('')
tentativa = int(input('Em qual número eu estou pensando? '))
print('PROCESSANDO')
sleep(2)

numero = randint(0,5)

if tentativa > 5:
    print('Eu falei entre 0 e 5! ;)')
elif tentativa == numero:
    print('Uau! Acertou em cheio! Estava pensando no {}!'.format(numero))
else:
    print('Você errou! Eu estava pensando no {}'.format(numero))

from random import randint
from time import sleep

jogada = ('Pedra', 'Papel', 'Tesoura')

print('=-' * 11)
print('Bem Vind@ ao Jokenpô!')
print('=-' * 11)

print('''
Escolha uma das opções abaixo:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA
''')

# Escolha do Humano
humano = int(input('Digita ai: '))

# Verificando se a escolha foi certa
while humano > 2:
    print('Poxa. Eu querendo brincar e você avacalhando...')
    print('Escolha de 0 a 2!!!!!')
    print('Repetindo...')
    humano = int(input('Manda: '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')
sleep(1)


print('Você escolheu {}!'.format(jogada[humano]))

# Escolha do Computador
computer = randint(0, 2)
print('Eu escolhi {}!'.format(jogada[computer]))

sleep(1)
if computer == 0:
    if humano == 0:
        print('EMPATAMOS!!! =)')
    if humano == 2:
        print('Ganhei! A Pedra esmaga a Tesoura!')
    elif humano == 1:
        print('Você ganhou! O Papel cobre a Pedra!')
elif computer == 1:
    if humano == 1:
        print('EMPATAMOS!!! =)')
    if humano == 2:
        print('Você ganhou! Tesoura corta papel!')
    elif humano == 0:
        print('Ganhei! O Papel cobre a Pedra')
elif computer == 2:
    if humano == 2:
        print('EMPATAMOS!!! =)')
    if humano == 0:
        print('Você ganhou! Pedra esmaga tesoura!')
    elif humano == 1:
        print('Ganhei! Tesoura corta papel!')

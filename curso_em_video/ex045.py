'''
Crie um programa que faça o computador jogar jokenpô com você.
'''
from random import randint
from time import sleep

print(13 * '=-')
print('Seja Bem Vind@ ao Jokempô')
print(13 * '=-')

print('Vamos jogar! =)')
print('''Escolha a sua opção:
[1] - Pedra
[2] - Papel
[3] - Tesoura''')

# Player choice
player = int(input('Qual opção você quer? '))

if player == 1:
    player = 'Pedra'
elif player == 2:
    player = 'Papel'
elif player == 3:
    player = 'Tesoura'
else:
    print('Opa! Opção inválida! \nTente Novamente.')

# Computer choice

computer = randint(1,3)

if computer == 1:
    computer = 'Pedra'
elif computer == 2:
    computer = 'Papel'
else :
    computer = 'Tesoura'

if player != 'Tesoura' and player != 'Papel' and player != 'Pedra':
    print('Poxa humano! Você não sabe brincar :(')
else:
    print('JOOO')
    sleep(1)
    print('KENNN')
    sleep(1)
    print('PÔ!!!')
    sleep(1)
    print('Eu escolho', computer)

    if computer == player:
        print('Deu EMPATE! Você escolheu {} e eu também! :)'.format(player, computer))
    elif computer == 'Pedra' and player == 'Tesoura':
        print('Eu ganhei \o/ ! A {} quebra a {}!'.format(computer, player))
    elif computer == 'Pedra' and player == 'Papel':
        print('Eu perdi! :( A {} é coberta pelo {}'.format(computer, player))
    elif computer == 'Tesoura' and player == 'Papel':
        print('Eu ganhei \o/ ! A {} corta o {}! '.format(computer, player))
    elif computer == 'Papel' and player == 'Pedra':
        print('Eu ganhei! =)~ O {} cobre a {}!'.format(computer, player))
    elif computer == 'Tesoura' and player == 'Pedra':
        print('Eu perdi! :( A {} é esmagada pela {}!'.format(computer, player))
    elif computer =='Papel' and player =='Tesoura':
        print('Eu perdi! :( O {} é cortado pela {}'.format(computer, player))

# Resolver o desafio 058 - Melhore o jogo do desafio 028. Onde o computador vai 
# "pensar" entre um número entre 0 e 10. Só que agora o jogador vai tentar 
# adivinhar até acertar. O programa deverá mostrar, no final, quantos palpites 
# foram necessários para venver.


from random import randint
from time import sleep

print('~' * 40)
print('Estou pensando em número entre 0 e 10.')
print('Você consegue adivinhar?')
print('~' * 40)
print('')
print('')
tentativa = int(input('Em qual número eu estou pensando? '))
print('PROCESSANDO')
sleep(2)

contador_palpites = 1
numero = randint(0,10)

while tentativa != numero:
    if tentativa < numero:
        tentativa = int(input('Pra cima!! Tente novamente =) '))
    if tentativa > numero:
        tentativa = int(input('Pra baixo! Diga um outro número! '))
    contador_palpites += 1
print('Parabéns! Você acertou. Eu estava pensando no número {}...'.format(numero))
print('Você deu {} palpites até acertar!'.format(contador_palpites))

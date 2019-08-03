#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Faça um programa que jogue par ou ímpar com o computador. O jogo só será
interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.
'''

from random import randint

vitorias = 0
print('SEJA BEM VIND@ AO JOGO DO PAR OU ÍMPAR!')
while True:
    print('~' * 20)
    numeroPessoa = int(input('Diga um número: '))
    paridade = str(input('Par ou Ímpar? [P/I]')).upper()
    if paridade in 'P/I':
        numeroComputador = randint(0,10)
        soma = numeroComputador + numeroPessoa
        verificador = soma % 2
        if verificador == 0 and paridade == 'P':
            print(f'{numeroPessoa} + {numeroComputador} é igual {soma}.')
            print('Você chutou par e ganhou!')
            vitorias += 1
        if verificador == 1 and paridade == 'I':
            print(f'{numeroPessoa} + {numeroComputador} é igual {soma}.')
            print('Você chutou ímpar e acertou!')
            vitorias += 1
        if verificador == 0 and paridade == 'I':
            print(f'Você errou. O número {soma} é par!')
            break
        if verificador == 1 and paridade == 'P':
            print(f'Você errou. O número {soma} é ímpar!')
            break
    else:
        print('Escolha inválida!!')
print(f'Você acertou {vitorias} vezes')

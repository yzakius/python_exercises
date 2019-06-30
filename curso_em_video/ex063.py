'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os
n primeiros elementos de uma Sequência Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8.
'''

# precisei de ajuda

termo = int(input('Qual o número de elementos da sequência? '))
t1 = 0
t2 = 1

print('{} -> {}'.format(t1,t2), end='')

contador = 3

while contador <= termo:
    t3 = t1 + t2
    print(' -> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    contador += 1
print('-> FIM')


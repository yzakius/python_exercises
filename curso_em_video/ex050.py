'''
Desenvolva um programa que leia 6 números inteiros. E mostre apenas a soma daqueles que forem pares.
'''
contador = 0
acumulador = 0
for i in range(1, 7):
    numero = int(input('Digite o {}º número: '.format(i)))
    if numero % 2 == 0:
        contador += 1
        acumulador += numero
print('Dos 6 números: {} são pares e a soma deles é {}!'.format(contador, acumulador))


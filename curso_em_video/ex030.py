''' 
Escreva um programa que leia um número inteiro e mostre se ele é par ou ímpar.
''' 

numero = int(input('Digite um número:' ))

if numero % 2 == 0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é ímpar!'.format(numero))

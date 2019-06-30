'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! 5x4x3x2x1 = 120
'''

print('~=' * 20)
print('Verificando o Fatorial')
print('~=' * 20)
numero = int(input('Digite um número qualquer: '))
acumulador = 1
inicial = numero
lista = []

print('Calculando {}! = '. format(numero), end='')
while numero > 0:
    print('{}'.format(numero), end='')
    print(' x ' if numero > 1 else ' =', end='')
    acumulador *= numero
    numero -= 1
print(' {}.'.format(acumulador))

    

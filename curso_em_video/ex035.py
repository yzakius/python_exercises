'''
Escreva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não, formar um triângulo.
'''

print('Escreva o comprimento de 3 retas!')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r2 - r3 < r1 < r2 + r3 and r1 - r3 < r2 < r1 + r3 and r1 - r2 < r3 < r1 + r2:
    print('Temos um TRIÂNGULO!')
else:
    print('NÃO é um triângulo!')


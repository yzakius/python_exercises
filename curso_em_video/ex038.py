'''
@python **Desafio 038** - Escreva um programa que leia **dois números**
inteiros e compare-os, mostrando na tabela uma mensagem: "o primeiro
valor é maior", "o segundo valor é menor",
"não existe valor maior, os números são iguais".
'''

print('Digite dois números inteiros!')
n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

if n1 > n2:
    print('{} é maior que {}'.format(n1, n2))
elif n1 < n2:
    print('{} é menor que {}'.format(n1, n2))
else:
    print('Os números são iguais!')


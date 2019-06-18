'''
escreva um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

menor = n1
if n2 < n1:
    menor = n2
if n3 < n2:
    menor = n3

maior = n2
if n2 > n1:
    maior = n2
if n3 > n2:
    maior = n3

print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))




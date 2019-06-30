'''
Crie um programa que leia o ano de nascimento de sete pessoas. 
No final ele deve mostrar quantas pessoas ainda não atingiram a maior idade e quantas já são maiores.
'''

from datetime import date

print('Digite o ano de nascimento de sete pessoas.')

maior = 0
menor = 0

for i in range(1, 7+1):
    ano = int(input('Digite o {}º ano: '.format(i)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('Existem {} pessoas maiores de idade.'.format(maior))
print('Existem {} pessoas menores de idade.'.format(menor))


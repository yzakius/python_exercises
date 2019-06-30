"""
Faça um programa que leia o peso de 5 pessoas e no final mostre o maior e o menor dos pesos lidos.
"""
# Precisei de ajuda

maior_peso = 0
menor_peso = 0
for i in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if i == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print('O maior peso é {} kg'.format(maior_peso))
print('O menor peso é {} kg'.format(menor_peso))


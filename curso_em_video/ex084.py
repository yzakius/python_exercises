"""
Faça um programa que leia o nome e peso de várias pessoas guardando tudo em uma lista.
No final ele tem que mostrar:

a) quantas pessoas foram cadastradas;
b) uma listagem com as pessoas mais pesadas;
c) uma listagem com as pessoas mais leves.
"""

pesos = []
pessoa = []
peso_maior = 0
peso_menor = 0
contpessoas = 0

while True:
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    if len(pesos) == 0:
        peso_maior = peso_menor = pessoa[1]
    else:
        if pessoa[1] > peso_maior:
            peso_maior = pessoa[1]
        if pessoa[1] < peso_menor:
            peso_menor = pessoa[1]
    pesos.append(pessoa[:])
    pessoa.clear()
    contpessoas += 1
    sair = str(input('Sair do Programa? [S/N]')).upper()
    if sair == 'S':
        break
print(f'Ao todo foram cadastradas {contpessoas} pessoas.')
print(f'O maior peso foi {peso_maior}kg de: ', end='')
for p in pesos:
    if p[1] == peso_maior:
        print(f'[{p[0]}]' , end='')
print()
print(f'O menor peso foi {peso_menor}kg de: ', end='')
for p in pesos:
    if p[1] == peso_menor:
        print(f'[{p[0]}]' , end='')
print()


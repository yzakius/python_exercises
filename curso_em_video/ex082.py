"""
Desafio 082
(OK) Crie um programa que leia vários números e coloque-os em uma lista.
Depois disso crie duas listas extras que vão conter apenas os valores pares
e os ímpares digitados respectivamente. Ao final mostre o conteúdo das três listas geradas.
"""

lista_numeros = []
lista_pares = []
lista_impares = []

while True:
    lista_numeros.append(int(input('Digite um número: ')))
    resposta = str(input('Quer continuar? [S/N]: '))
    if resposta in 'Nn':
        break
# Separando as Listas
for numero in lista_numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'A lista TOTAL: {lista_numeros}')
print(f'Lista de números PARES: {lista_pares}')
print(f'Lista de números ÍMPARES: {lista_impares}')

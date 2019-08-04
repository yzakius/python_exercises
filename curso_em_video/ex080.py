"""
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista_ordenada já na posição correta de inserção (sem usar o
sort). No final mostre a lista_ordenada ordenada na tela.
"""

lista_ordenada = []

for numero in range(0, 5):
    n = int(input('Digite um número: '))
    if lista_ordenada == []:
        lista_ordenada.append(n)
    elif n > max(lista_ordenada):
        lista_ordenada.append(n)
    elif n < min(lista_ordenada):
        lista_ordenada.insert(0, n)
print(lista_ordenada)
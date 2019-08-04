"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
"""
lista = []

for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)

minimo = min(lista)
maximo = max(lista)

print(lista)

print(f'O menor valor digitado foi {minimo} e está na {lista.index(minimo) + 1}ª posição da lista.')
print(f'O maior valor digitado foi {maximo} e está na {lista.index(maximo) + 1}ª posição da lista.')
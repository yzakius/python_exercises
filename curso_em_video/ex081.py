"""
Crie um programa que leia vários números e coloque-os em uma lista. Depois disso, mostre:
A) Quantos números foram digitados;
B) A lista de valores ordenada de forma decrescente;
C) Se o valor 5 foi digitado e está ou não na lista.
"""

contador_numeros = 0
contador_de_cinco = 0
lista_ordenada = []

while True:
    n = int(input('Digite um número qualquer (999 sai do programa): '))
    if n == 999:
        break
    if n == 5:
        contador_de_cinco += 1
    contador_numeros += 1
    lista_ordenada.append(n)

print('-=' * 12)
print(f'Você digitou {contador_numeros} números')
print(f'A lista em ordem descrescente fica: {sorted(lista_ordenada, reverse=True)}')
if 5 in lista_ordenada and contador_de_cinco > 0:
    print(f'A lista contém o número 5 digitado {contador_de_cinco} vezes.')
else:
    print('A lista não contém o número 5.')
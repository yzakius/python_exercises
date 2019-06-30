'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os
10 primeiros termos da progressão utilizando a estrutura while.
'''
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = termo
decimo = contador + 10

while contador < decimo:
    print(termo, '-> ', end='')
    termo = termo + razao
    contador += 1
print('FIM')


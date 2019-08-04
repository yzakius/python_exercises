"""
Crie um programa onde o usuário pode digitar vários valores numéricos
e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será
adicionado. No final, serão exibidos todos os valores únicos digitados em ordem crescente.
"""

lista = []

while True:
    valor = int(input('Digite um valor: '))
    chave = str(input('Continuar? [S/N]: '))
    if chave in 'Nn':
        break
    if valor not in lista:
        lista.append(valor)
print(f'O ordenamento da lista é: {sorted(lista)}')

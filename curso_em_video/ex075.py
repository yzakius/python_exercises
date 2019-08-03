# recebendo os valores da variáveis
valor1 = int(input('Valor 1: '))
valor2 = int(input('Valor 2: '))
valor3 = int(input('Valor 3: '))
valor4 = int(input('Valor 4: '))

# transformando as variáveis em tuplas
valor_tupla = (valor1, valor2, valor3, valor4)

# Teste 1: contando a quantidade de ocorrências do número 9
print(f'Quantidade de números 9: {valor_tupla.count(9)}')

# Teste 2: localizando a primeira ocorrência do número 3
if 3 in valor_tupla:
     print(f'A primeira ocorrência de 3 está na {valor_tupla.index(3) + 1}ª posição.')
else:
     print('Não contém número 3!')

# Teste 3: imprimindo os números pares.
eh_par = []

for i in valor_tupla:
    if i % 2 == 0:
        eh_par.append(i)
eh_par = tuple(eh_par)
print(f'Os números pares são: {eh_par}')

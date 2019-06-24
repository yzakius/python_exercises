#Faça um programa que leia um número inteiro 
#e diga se ele é, ou não, se ele é primo.

# exercício resolvido com ajuda!

numero = int(input('Digite um número: '))
contador = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[33m{}\033[m'.format(c), end=' ')
        contador += 1
    else:
        print('\033[m{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes'.format(numero, contador))
if contador == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')


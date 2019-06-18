'''
@python **Desafio 037** - Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a **base de conversão**: 1 - binário, 2 - octal, 3 - hexadecimal. *dica:* o python faz isso sozinho.
'''

numero = int(input('Digite um número: '))
escolha = int(input('''Escolha uma Base de conversão:
-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
1 - Binário
2 - Octal
3 - Hexadecimal'''))

if escolha == 1:
    print('O número {} é {} em binário'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('O número {} é {} em octal'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O número {} é {} em hexadecimal'.format(numero, hex(numero)[2:]))
else:
    print('Opção inválida!')

'''
Resolver o desafio 059 - Crie um programa que leia 2 valores e mostre um menu na tela:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
O seu programa devará realizar a operação solicitada em cada caso.
'''

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))

menu = 0

while menu != 5:
    print('>>>>>>> Escolha uma das opções abaixo!')
    print('')
    menu = int(input('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa

    Opção desejada: '''))

    if menu == 5:
        print('Saindo do programa...')
    elif menu == 1:
        soma = valor1 + valor2
        print('')
        print('~' * 25)
        print('SOMANDO  OS  VALORES')
        print('{} + {} = {}'.format(valor1, valor2, soma))
        print('~' * 25)
        print('')
    elif menu == 2:
        multiplica = valor1 * valor2
        print('')
        print('~' * 25)
        print('MULTIPLICANDO  OS  VALORES')
        print('{} * {} = {}'.format(valor1, valor2, multiplica))
        print('~' * 25)
        print('')
    elif menu == 3:
        if valor1 > valor2:
            print('O maior número é: {}'.format(valor1))
        elif valor2 > valor1:
            print('O maior número é: {}'.format(valor2))
        else:
            print('Os números são iguais!')
        print('~' * 25)
        print('')
    elif menu == 4:
        valor1 = float(input('Digite um valor: '))
        valor2 = float(input('Digite outro valor: '))
        print('')
        print('Valores atualizados!')
    else:
        print('Digite uma das opções fornecidas pelo programa!')

'''
Refazer o desafio 009, mostrando a tabuada de um número de usuário, só que agora com o for.
'''

numero1 = int(input('Número para multiplicar: '))
numero2 = int(input('Quantidade de multiplicações: '))
contador = 0
for i in range(0, numero2):
    contador += 1
    print('{} x {:2} = {}'.format(numero1, contador, numero1 * contador))


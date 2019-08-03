'''
Faça um programa que mostre a tabuada de vários números.
Um para cada valor digitado pelo usuário. O programa será
interrompido quando o número solicitado for negativo.
'''
print('Utilize um número negativo para sair')
numero = int(input('Digite um número: '))

while numero > -1:
    for i in range(1,11):
        print(f'{numero} X {i} = {numero * i}')
        i = i + 1
    print('~' * 17)
    print('Utilize um número negativo para sair')
    numero = int(input('Digite um novo número: '))
print('Obrigado e Volte Sempre!')


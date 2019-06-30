'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só
vai parar quandoo usuário digitar o valor 999, que é a condição de parada. No
final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).
'''

print('-' * 20)
print('Somador de Números')
print('-' * 20)

chave = True
somador = 0
contador = 0

while chave == True:
    numero = int(input('Digite um número: '))
    print('Digite 999 para parar o programa!')
    if numero != 999:
        somador = numero + somador
        contador += 1
        chave = True
    else:
        chave = False
        print('Saindo...')
print('~' * 20)
print('Você digitou {} números!'.format(contador))
print('A soma dos números digitados é: {}'.format(somador))
print('~' * 20)


'''
Faça um programa que calcule a soma entre todos os números ímpares que são múltplos de 3 e que encontram no intervalo de 1 até 500.
'''
soma = 0

for numero in range(1,501, 2):
    if numero % 3 == 0:
        print(numero, end=' ')
        soma = soma + numero
print('A soma total dos números é: {}'.format(soma))


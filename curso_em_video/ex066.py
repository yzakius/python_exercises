'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é a
condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando a flag).
'''

contador = 0
somador = 0

while True:
    print('-=' * 17)
    numero = int(input('Digite um valor [999 p/ sair]: '))
    if numero != 999:
        contador += 1
        somador = somador + numero
    else:
        break
print(f'Você digitou {contador} números. A soma entre eles é {somador}.')



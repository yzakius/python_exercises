'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve
perguntar ao usuário se ele quer, ou não continuar a digitar os valores.
'''
key = True
acumulador = 0
contador = 0
maior = 1
menor = 1

while key == True:
    numero = int(input('Digite 0 para sair ou Digite um número inteiro: '))
    if numero != 0:
        acumulador += numero
        contador += 1
        if contador == 1:
            maior = numero
            menor = numero
        elif maior < numero:
            maior = numero
        elif menor > numero:
            menor = numero
    else:
        key = False
media = acumulador / contador
print('A média entre os valores digitados é {}.'.format(media))
print('O maior valor é {}!'.format(maior))
print('O Menor valor é {}!'.format(menor))


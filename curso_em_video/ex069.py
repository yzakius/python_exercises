'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário que ou não continuar. No
final, mostre: a) quantas pessoas tem mais de 18 anos, b) quantos homens foram
cadastrados, c) quantas mulheres tem menos de 20 anos.
'''

contadorMaiores = contadorHomens = contadorMulheresMenores = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
    if idade > 18:
        contadorMaiores += 1
    if sexo == 'M':
        contadorHomens += 1
    if idade < 20 and sexo == 'F':
        contadorMulheresMenores += 1
    print('Dados salvos!')
    print('=-' * 13)
    continuar = str(input('Deseja continuar?[S/N]')).upper()
    if continuar == 'N':
        break
print('~' * 13)
print(f'Existem {contadorMaiores} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {contadorHomens} homens.')
print(f'Existem {contadorMulheresMenores} mulheres menores que 20 anos.')

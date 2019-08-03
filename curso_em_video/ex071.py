'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o
caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('Seja Bem VIND@ ao Banco')
print('\/' * 20)
saque = int(input('Digite o valor do saque R$: '))
saldoFinal = saque

totalCem = totalCinquenta = totalVinte = totalDez = totalUm = 0
totalCem = saldoFinal // 100
saldoFinal = saldoFinal % 100
totalCinquenta = saldoFinal // 50
saldoFinal = saldoFinal % 50
totalVinte = saldoFinal // 20
saldoFinal = saldoFinal % 20
totalDez = saldoFinal // 10
saldoFinal = saldoFinal % 10
totalUm = saldoFinal // 1
saldoFinal = saldoFinal % 1
print(f'Total de cédulas de R$100,00: {totalCem}')
print(f'Total de cédulas de R$50,00: {totalCinquenta}')
print(f'Total de cédulas de R$20,00: {totalVinte}')
print(f'Total de cédulas de R$10,00: {totalDez}')
print(f'Total de cédulas de R$1,00: {totalUm}')


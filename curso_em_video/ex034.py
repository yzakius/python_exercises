'''
@python **Desafio 034:** escreva um programa que pergunte o salário
de um funcionário e calcule o valor do seu aumento.
Para salários superiores a 1250 calcule um aumento de 10%.
Para os inferiores ou iguais o aumento é de 15%.
'''

salario = float(input('Qual o valor do salário do funcionário? '))

if salario > 1250:
    novosalario = salario + (salario * 0.1)
    aumento = '10%'
else:
    novosalario = salario + (salario * 0.15)
    aumento = '15%'

print('O funcionário recebeu um aumento de {} e seu novo salário é de R${:.2f}'.format(aumento, novosalario))


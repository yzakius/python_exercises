'''
@python **Desafio 036** - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o **valor da casa**, o **salário** do comprador e em **quantos anos** ele vai pagar. Calculer o valor da prestação mensal sabendo que ela não pode exceder **30%** do salário ou então o empréstimo será negado.
'''

valor = float(input('Valor do imóvel R$:  '))
salario = float(input('Salário do comprador R$:' ))
anos = int(input('Anos de pagamento: ')) 

prestacao = valor / (anos * 12)
verificador = salario * (30 / 100)

if prestacao <= verificador:
    print('Empréstimo \033[30;42mAPROVADO!\033[m')
else:
    print('Empréstimo \033[30;41mNEGADO!\033[m')
    print('A prestação fica acima do permitido (30% do salário)')



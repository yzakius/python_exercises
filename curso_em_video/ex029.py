'''
@python **Desafio 029:** escreva um programa que leia a velocidade de um carro. Se ele ultrapassar a velocidade de 80km mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite.
'''

velocidade = float(input('Digite a velocidade do carro: '))

if velocidade > 80:
    print('Você foi multado!')
    valor = (velocidade - 80) * 7
    print('Você estava a {} km/h. A multa será de R${:.2f} reais'.format(velocidade, valor))
else:
    print('Continue respeitando os limites de velocidade ;) ')
    

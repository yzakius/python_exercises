'''
escreva um programa que pergunte a distância de uma viagem em km. Calcular o preço da passagem cobrando 0.50 para cada km até 200km. E 0.45 para viagens mais longas.
'''

distancia = int(input('A viagem é de quantos KM? '))

if distancia <= 200:
    valor = distancia * 0.50
    print('A viagem custará R${:.2f} reais.'.format(valor))
else:
    valor = distancia * 0.45
    print('A viagem custará R${:.2f} reais.'.format(valor))


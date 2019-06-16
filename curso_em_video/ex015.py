km = float(input('Digite a kilometragem percorrida com o carro: '))
dias = int(input('digite a quantidade dias de alguel do carro: '))

preco = (60 * dias) + (km * 0.15)

print('Por {} dias com o carro e a kilometragem de {}km o preço do alguel do carro será de R${:.2f} reais'.format(dias, km, preco))

altura = float(input('Digite a altura da parede: '))
largura = float(input('Agora digite a largura: '))
quadrado = altura * largura
pintura = quadrado / 2
print('Para pintar uma área de {} m² você precisará de {:.2f} litros de tinta'.format(quadrado, pintura))

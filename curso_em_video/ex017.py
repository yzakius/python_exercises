'''
from math import hypot

opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
print(hypot(opo, adj))

'''
# Solução sem biblioteca
opo = float(input('Digite o comprimento do cateto oposto: '))
adj = float(input('Digite o comprimento do cateto adjacente: '))
hipo = ((opo ** 2) + (adj ** 2)) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipo))

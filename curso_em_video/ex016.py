"""
from math import trunc

num = numat(input('Digite um número qualquer: '))
print('A porção inteira de {} é igual a {}'.format(num, trunc(num)))
"""

# Resolução sem importar biblioteca

num = float(input('Digite um número qualquer: '))
print('A porção inteira de {} é igual a {}'.format(num, int(num)))

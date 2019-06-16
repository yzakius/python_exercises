'''
numero = input('Digite um número de 0 a 9999: ')
numero = list(numero)

print('Milhar:  {}'.format(numero[0]))
print('Centena: {}'.format(numero[1]))
print('Dezena:  {}'.format(numero[2]))
print('Uidade:  {}'.format(numero[3]))
'''

num = int(input('Digite um número: '))
print('Analisando o número {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))

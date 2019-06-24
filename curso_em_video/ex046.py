'''
Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artifício. Ele vai de 10 até 0 com uma pausa de 1 segundo entre eles.
'''


from time import sleep

# Minha Solução

'''
print('Iniciando a contagem regressiva para a queima de fogos!')

x = 10

for i in range(0, 11):
    print(x)
    sleep(1)
    x -= 1
print('FELIZ ANO NOVO!')
'''

# Solução do Professor

print('Iniciando a contagem regressiva para a queima de fogos!')

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('BOM! BOOOMM! POW! POW!')

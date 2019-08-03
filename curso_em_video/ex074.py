from random import randint

number_list = []

for i in range(0,5):
    number_list.append(randint(0, 99))

number_list = tuple(number_list)
print('Números Gerados')
print('*' * 20)

for listagem, numero in enumerate(number_list):
    print(f'{listagem + 1}º: {numero}')

print('*' * 20)
print(f'Maior número: {max(number_list)}')
print(f'Menor número: {min(number_list)}')

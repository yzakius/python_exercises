produtos = ('Maracujá (UN)', 1.00,
            'Coentro (molho)', 2.50,
            'Pão Cenoura e Cebola (UN)', 10.00)

print('-' * 50)
print(f'{"Listagem de Preços":^50}')
print('-' * 50)

for produto in range(0, len(produtos)):
    if produto % 2 == 0:
        print(f'{(produtos[produto]):.<40}', end='')
    else:
        print(f'R$ {produtos[produto]:>7.2f}')

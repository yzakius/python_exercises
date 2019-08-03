'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá
perguntar se o usuário vai continuar. No final, mostre: a) qual é o total gasto
na compra, b) quantos produtos custam mais de R$1.000,00 reais, c) qual é o nome
do produto mais barato.
'''
print('{:-^40}'.format(' MERCADÃO DO JOÃO '))

totalCompra = contadorProdutos = preçosMaioresMil = menorPreço = 0
menorPreçoProduto = ''

while True:
    produto = str(input('Nome do produto: ')).upper()
    preço = float(input('Preço R$: '))
    print('Produto adicionado com sucesso!')
    totalCompra += preço
    contadorProdutos += 1
    if preço > 1000:
        preçosMaioresMil += 1
    if contadorProdutos == 1:
        menorPreço = preço
        menorPreçoProduto = produto
    if menorPreço > preço:
        menorPreço = preço
        menorPreçoProduto = produto
    print('~' * 12)
    continuar = str(input('Quer colocar mais um produto na cesta? [S/N]')).upper()
    if continuar == 'N':
        break
print(f'Total da compra: R${totalCompra:.2f}')
print(f'Produtos acima de R$1.000,00: {preçosMaioresMil}')
print(f'O produto mais barato: {menorPreçoProduto} - R${menorPreço:.2f} reais')

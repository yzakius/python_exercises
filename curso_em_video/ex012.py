preco = float(input('Digite o preço do produto R$ : '))
desconto = preco - (preco * 5 / 100)
print('Com 5% de desconto o novo preço é de R${:5.2f} reais'.format(desconto))

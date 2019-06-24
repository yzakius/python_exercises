'''
Elabore um programa que calcule o valor  ser pago por um compra considerando o seu preço normal e a condição de pagamento: à vista, 10% de desconto; à vista no cartão, 5% de desconto; em até 2x no cartão, preço normal; 3x ou mais, 20% de juros.
'''

print('{:=^40}'.format(' Lojão da Economia '))
preco = float(input('Digite o Valor das Compras: '))
pagamento = int(input('''Escolha a condição de pagamento:
    [1] - À Vista: Dinheiro ou Cheque
    [2] - À Vista: Cartão
    [3] - À Prazo: 2x no Cartão
    [4] - À Prazo: 3x ou mais no Cartão'''))

if pagamento == 1:
    novo_preco = preco - (preco * 10 / 100)
    print('Pagamento à vista recebe desconto de 10%. A compra ficará por R${:.2f} reais'.format(novo_preco))
elif pagamento == 2:
    novo_preco = preco - (preco * 5 / 100)
    print('Desconto de 5%. A compra ficará por R${:.2f} reais!'.format(novo_preco))
elif pagamento == 3:
    print('Não há desconto para esse tipo de pagamento.')
elif pagamento == 4:
    novo_preco = preco + (preco * 20 / 100)
    print('Houve um acréscimo de 20%. A compra ficará por R${:.2f} reais'.format(novo_preco))
else:
    print('Opção inválida!')

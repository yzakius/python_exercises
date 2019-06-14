n = int(input('Digite um número: '))
print('O dobro de {} é {}'.format(n, n * 2))
print('O triplo de {} é {}'.format(n, n * 3))
print('A raiz quadrada de {} é {:.2f}'.format(n, n ** (1/2)))

# Função para Raiz Quadrada
print('Utilizando a função pow podemos chegar a raiz quadrada de {:.2f}'.format(pow(n, (1/2))))

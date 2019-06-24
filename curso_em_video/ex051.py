
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética. 
# No final mostre os 10 primeiros termos dessa PA.

#Minha solução
#termo = int(input('Digite o primeiro termo da PA: '))
#razao = int(input('Digite a razão da PA: '))
#for i in range(termo, termo + 10):
#    termo = termo + razao
#    print('{}'.format(termo), end=' ')

# Solução de Guanabara

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao # aqui é para calcular o décimo termo (ele teve que apelar para a matemática)
for c in range(termo, decimo + razao, razao): # inicio, fim da range, pulos
    print('{}'.format(c), end='-> ')
print('Acabou')

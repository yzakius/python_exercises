'''
@python **Desafio 040** -
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
acima de 5, reprovado; entre 5 e 6.9, recuperação, 7 ou superior, aprovado.
'''

print('Entre com as notas do aluno: ')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1 + n2) / 2

if media >= 7.0:
    print('Parabéns! Você foi aprovado por média. \nMédia {}'.format(media))
elif media >= 5 and media <= 6.9:
    print('Você está em Recuperação. Estude mais! \nMédia {}'.format(media))
else:
    print('Você foi reprovado! Agora só no próximo ano. \nMédia {}'.format(media))

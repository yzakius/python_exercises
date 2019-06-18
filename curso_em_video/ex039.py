
'''
@python **Desafio 039** - Faça um programa que leia de nascimento
de um jovem e informe, de acordo com a sua idade:
1 - se ele ainda vai se alistar,
2 - se é hora de se alistar,
3 - se já passou da hora de se alistar.
**O programa** também deverá mostrar o tempo restante ou
o tempo expirado do prazo. (pegar do sistema)
'''
from datetime import date

ano_nascimento = int(input('Qual o ano do seu nascimento: '))

ano_atual = date.today().year

alistamento = ano_atual - ano_nascimento

if alistamento == 18:
    print('Chegou a hora da Farsa Militar!')
elif alistamento < 18:
    print('Você ainda não tem idade. Aguarde {} anos para poder se alistar.'.format(18 - alistamento))
else:
    print('Você deveria ter se alistado há {} anos!'.format(alistamento - 18))



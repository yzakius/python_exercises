'''
@python **Desafio 041** -
A confederação Nacional de Natação precisa de um
programa que leia o ano de nascimento de um atleta e
mostre sua categoria (de acordo com a sua idade).
mirim; até 14,
infantil; até 19,
junior; até 20,
senior; acima, master.
'''
from datetime import date

ano_nascimento = int(input('Entre com ano de nascimento do atleta: '))
ano_atual = date.today().year

categoria = ano_atual - ano_nascimento

if categoria <= 9:
    print('O atleta competirá na categoria Mirim')
elif categoria <= 14:
    print('O atleta competirá na categoria Infantil')
elif categoria <= 19:
    print('O atleta competirá na categoria Junior')
elif categoria <=20:
    print('O atleta competirá na categoria Sênior')
else:
    print('O atleta competirá na categoria Master')



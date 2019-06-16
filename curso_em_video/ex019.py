from random import choice

aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4]

print('Sortendo @ felizard@....')
sortudx = choice(lista)

print('Opa {}! Você é @ sortud@ que vai apagar o quadro ;)'.format(sortudx))

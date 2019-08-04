"""
Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta.
"""

def expressao(parenteses):
    checagem = list(parenteses)
    if checagem.count('(') == checagem.count(')'):
        print('A expressão está correta!')
    else:
        print('A expressão está incorreta!')

expressao(input(str('Digite uma expressão usando parênteses: ')))

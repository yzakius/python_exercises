"""
Criar um programa que conte caracteres de uma string através de uma lista.
"""


def conta_caracteres(s):
    """
    Função que conta os caracteres de uma string.
    Exemplo:
    >>> conta_caracteres('isaac')
    a: 2
    c: 1
    i: 1
    s: 1
    >>> conta_caracteres('banana')
    a: 3
    b: 1
    n: 2
    :param s: string a ser contada
    """
    caracteres_ordenados = sorted(s)
    caractere_anterior = caracteres_ordenados[0]
    contagem = 1

    for caractere in caracteres_ordenados[1:]:
        if caractere == caractere_anterior:
            contagem += 1
        else:
            print(f'{caractere_anterior}: {contagem}')
            caractere_anterior = caractere
            contagem = 1
    print(f'{caractere_anterior}: {contagem}')


if __name__ == '__main__':
    conta_caracteres('isaac')
    print()
    conta_caracteres('banana')

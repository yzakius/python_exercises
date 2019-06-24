"""
Criar um programa que conte caracteres de uma string através de um dicionário.
"""


def conta_caracteres(s):
    """
    Função que conta os caracteres de uma string.
    Exemplo:
    >>> conta_caracteres('isaac')
    {'a': 2, 'c': 1, 'i': 1, 's': 1}
    >>> conta_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}
    :param s: string a ser contada
    """

    resultado = {}

    # Com o uso de variáveis auxiliares
    # for caractere in s:
    #     contagem = resultado.get(caractere, 0)  # passando um valor default caso o elemento não seja encontrado
    #     contagem += 1
    #     resultado[caractere] = contagem
    # return resultado

    # Sem o uso de variáveis auxiliares
    for caractere in s:
        resultado[caractere] = resultado.get(caractere, 0) + 1
    return resultado


if __name__ == '__main__':
    print(conta_caracteres('isaac'))
    print()
    print(conta_caracteres('baana'))

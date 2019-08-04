palavras = ('anti-cimex', 'amebix', 'bauhaus', 'queen')

x = 0
for unidade in palavras:
    print(f'A palavra {unidade} possui as vogais: ', end='')
    for letra in palavras[x]:
        if letra in 'aeiou':
            print(f'{letra}', end='')
    x += 1
    print('')

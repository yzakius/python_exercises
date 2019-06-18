'''
**Desafio 042** -
Refaça o desafio 035 dos triângulos.
Veja se é equilátero, isósceles e escaleno.
'''
print('Escreva o comprimento de 3 retas!')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Temos um TRIÂNGULO!')
    if r1 == r2 and r2 == r3: # o python permite: r1 == r2 == r3 (exemplo)
        print('EQUILÁTERO')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('NÃO é um triângulo!')

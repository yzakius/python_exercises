'''
Desafio 026 - Faça um programa que leia uma frase pelo teclado e mostre: quantas vezes aparece a letra 'A', em que posição ela aparece na primeira vez, em que posição ela aparece na última vez.

# minha resposta

frase = str(input('Digite uma frase: ')).strip()

igual = frase.upper()

print("A letra 'A' aparece {} vezes.".format(igual.count('A')))
print('A sua primeira ocorrência é na posição {}.'.format(igual.find('A')))
print('A sua última ocorrência é na posição {}.'.format(igual.rfind('A')))
'''

# Solução do professor

frase = str(input('Digite uma frase: ')).upper().strip()
print("A letra 'A' aparece {} vezes.".format(frase.count('A')))
print('A sua primeira ocorrência é na posição {}.'.format(frase.find('A') + 1))
print('A sua última ocorrência é na posição {}.'.format(frase.rfind('A') + 1))

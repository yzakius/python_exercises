# Faça um programa que leia o sexo de uma pessoa. 
# Mas só aceita M ou F. Caso esteja errado, peça a 
# digitação novamente até ficar certo.

# Fiz com ajuda

sexo = str(input('Digite o sexo. Utilize [F/M] ')).strip()[0] # O zero é um fatiamento

while sexo not in 'MmFf':
    print('Por favor. Utilize F ou M.')
    sexo = str(input('Digite o sexo: ')).strip()[0]
print('O sexo escolhido foi {}.'.format(sexo))

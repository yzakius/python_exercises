# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo. 
# (desconsidere os acentos). O seu programa tirará os espaços. =)


# Exercicio com Ajuda (eu não sabia retirar os espaços)

frase = str(input('Digite uma frase: ')).strip().upper()

# Fazendo um split
palavras = frase.split()

# Juntando as plavras
junto = ''.join(palavras)

inverso = junto[::-1]

#for letra in range(len(junto) -1, -1, -1):
#    inverso += junto[letra]
#
print(junto, inverso)

if junto == inverso:
    print('Temos um Palíndromo!')
else:
    print('Não é um Palíndrromo!')

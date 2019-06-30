"""
Desenvolva um programa que leia: nome, idade e sexo de 4 pessoas. 
No final o programa deve mostrar: media de idade, nome do homem mais velho e quantas mulheres tem menos de 20 anos.
"""

print('Digite os dados abaixo!')

contador_idade = 0
contador_mulheres = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''

for pessoa in range(1, 5):
    print('=-' * 14)
    print('Dados do {}º indivíduo.'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade (apenas números): '))
    contador_idade += idade
    genero = str(input('Gênero (escolha M ou F): ')).strip()
    if genero in 'Mm':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome
    if genero in 'Fm':
        if idade < 20:
            contador_mulheres += 1

print('=-' * 23)
print('A médida das idades é {} anos.'.format(contador_idade / 4))
print('O homem mais velho é {} e ele tem {} anos.'.format(nome_homem_mais_velho, idade_homem_mais_velho))
print('Existem {} mulheres menores que 20 anos.'.format(contador_mulheres))



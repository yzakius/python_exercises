# Resposta do Professor

# cidade = str(input('Digite o nome de uma cidade: ')).strip()
#
# print(cidade[:5].upper() == 'SANTO')
# Minha resposta

cidade = str(input('Digite o nome de uma cidade: '))

teste = cidade.split()
teste2 = 'Santo' in teste[0]

print('O nome da cidade é {}'.format(cidade))
print('A cidade começa com "Santo": {}'.format(teste2))

print(cidade)
print(teste)


times = ('Palmeiras', 'Cruzeiro', 'Grêmio', 
         'Santos', 'Atlético Mineiro', 'Corinthians',
         'Flamengo', 'Botafogo', 'Atlético Paranaense',
         'Internacional', 'São Paulo', 'Fluminense',
         'Vasco da Gama', 'Chapecoense', 'Sport',
         'Ponte Preta', 'Coritiba', 'Vitória', 
         'Figueirense', 'Atlético Goianiense')

print('=' * 32)
print('CAMPEONATO BRASILEIRO - 2018')
print('=' * 32)

print('Os 5 Primeiros Colocados:')
print('~' * 32)
for colocacao, colocado in enumerate(range(0, 5)):
    print(colocacao + 1, times[colocado])
print('=' * 32)
print('Os 4 Últmos Colocados')
print('~' * 32)
for colocado in range(16, 20):
    print(times[colocado])
print('=' * 32)
print('Os 20 times em Ordem Alfabética')
print('~' * 32)
print(sorted(times))
print('=' * 32)
for colocacao, colocado in enumerate(range(0, 20)):
    if times[colocado] == 'Chapecoense':
        chape = colocacao + 1
print(f'A Chapecoense está na {chape}ª colocação')
print('~' * 32)

'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar
mais alguns termos. O programa encerra quando disser que quer mostrar
0 termos.
'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Finalizada! Ao todo foram mostrados {} termos.'.format(total))

 

# Minha resolução
# termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razão da PA: '))
# contador = termo
# decimo = contador + 10
# 
# while contador < decimo:
#     print(termo, '-> ', end='')
#     termo = termo + razao
#     contador += 1
# print('FIM')
# print('-=' * 22)
# 
# menu = 1
# novo_contador = 0
# 
# while menu != 0:
#     menu = int(input('''
#     Digite um novo número para mostrar mais termos;
#     Ou digite 0 (zero) para sair
#     '''))
#     novo_termo = menu
#     if menu != 0:
#         while novo_contador < menu:
#             print(novo_termo, '-> ', end='')
#             novo_termo = novo_termo + razao
#             novo_contador += 1
#     else:
#         print('Xau amigo!')

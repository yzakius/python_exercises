contagem = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito', 'nove',
            'dez', 'onze', 'doze', 'treze', 'catorze',
            'quinze', 'dezeseis', 'dezesete', 'dezoito',
            'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número [0 a 20]: '))
    if numero >= 0 and numero <=20:
        print(f'Você digitou o número {contagem[numero]}!')
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar == 'N':
            print('Até mais!')
            break
        elif continuar not in 'SN':
            print('Tente novamente!')
    else:
        print('Entrada Inválida! Tente novamente.')


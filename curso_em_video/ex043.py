'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o seu IMC e mostre o status de acordo com a tabela abaixo: abaixo de 18.5, abaixo do peso; entre 18.5 e 25, peso ideal; 25 até 30, sobrepeso; 30 até 40, obesidade; acima de 40 obesidade mórbida.
'''

nome = str(input('Digite o nome do paciente: '))
peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))

imc = peso / (altura ** 2)
print(imc)

if imc < 18.5:
    print('Olá {}. Seu IMC é {:.2f} e você está Abaixo do Peso!'.format(nome, imc))
elif imc >= 18.5 and imc < 25:
    print('Olá {}. Seu IMC é {:.2f} e você está com o Peso Ideal!'.format(nome, imc))
elif imc >= 25 and imc < 30:
    print('Olá {}. Seu IMC é {:.2f} e você está Acima do Peso!'.format(nome, imc))
elif imc >= 30 and imc < 40:
    print('Olá {}. Seu IMC é {:.2f} e você está com Obesidade!'.format(nome, imc))
else:
    print('Olá {}. Seu IMC é {:.2f} e você está com Obesidade Mórbida!'.format(nome, imc))


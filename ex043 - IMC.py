# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# Entre 25 e 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade mórbida

titulo = 'Vamos calcular seu IMC'
print('=' * 28)
print(titulo.center(28))
print('=' * 28)
peso = float(input('Qual seu peso? (kg) '))
altura = float(input('Qual sua altura? (m) '))
IMC = peso / (pow(altura, 2))
print('=' * 28)
print('Seu IMC é {:.2f}\nSTATUS: '.format(IMC), end='')
if IMC < 18.5:
    print('abaixo do peso')
elif 18.5 <= IMC < 25:
    print('peso ideal')
elif 25 <= IMC < 30:
    print('sobrepeso')
elif 30 <= IMC < 40:
    print('obesidade')
else:
    print('obesidade mórbida')
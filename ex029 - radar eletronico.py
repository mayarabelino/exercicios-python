# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada km acima do limite.

v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('O limite da via é de 80km/h. Você foi multado!')
    multa = (v - 80) * 7.00
    print('O valor da multa é R${:.2f}.'.format(multa))
else:
    print('Você está dentro do limite permitido!')
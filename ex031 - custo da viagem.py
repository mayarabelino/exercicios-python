# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$ 0,45 para viagens mais longas.

dist = float(input('Qual é a distância da sua viagem? '))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.45
print('O valor da viagem é R${:.2f}'.format(valor))
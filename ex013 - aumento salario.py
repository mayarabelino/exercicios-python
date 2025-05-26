# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com aumento de 15%
s = float(input('Qual sálario atual do funcionário? R$'))
sa = s + (s * 0.15)
print('O novo salário com aumento de 15% é R${:.2f}.'.format(sa))
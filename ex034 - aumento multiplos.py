# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual seu salário? R$'))
if salario > 1250.00:
    a = salario + (salario * 0.10)
else:
    a = salario + (salario * 0.15)
print('Com o aumento seu salário vai ficar R${:.2f}'.format(a))
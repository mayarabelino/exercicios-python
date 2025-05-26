# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quatos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
casa = float(input('Qual valor da casa? R$'))
salario = float(input('Qual seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))
parcela = casa / (anos * 12)  # valor da prestação
emp = salario * 0.30  # 30% do salário
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f} mensais.'.format(parcela))
if parcela <= emp:
    print('Empréstimo {}APROVADO{}!'.format(cores['verde'], cores['limpa']))
else:
    print('Empréstimo {}NEGADO{}!'.format(cores['vermelho'],cores['limpa']))

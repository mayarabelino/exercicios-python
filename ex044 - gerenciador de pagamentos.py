# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e a condição de pagamento:
# Á vista dinheiro ou pix: 10% de desconto
# Á vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

valor = float(input('Digite o valor da compra: R$'))
print('-' * 28)
print('{:^28}'.format('Opções de pagamento:'))
print('-' * 28)
print('''[1] Dinheiro ou Pix
[2] Débito
[3] Crédito, em até 2x
[4] Crédito, 3x ou mais''')
print('-' * 28)
escolha = int(input('Digite a opção desejada: '))
print('-' * 28)
if escolha == 1:
    final = valor - (valor * 0.10)
elif escolha == 2:
    final = valor - (valor * 0.05)
elif escolha == 3:
    final = valor
    parcela2 = final / 2
    print('Em 1x fica R${:.2f} sem juros\nEm 2x fica R${:.2f} sem juros'.format(final, parcela2))
elif escolha == 4:
    final = valor + (valor * 0.20)
    parcelas = int(input('Informe a quantidade de parcelas (máximo 10x): '))
    precox = final / parcelas
    if parcelas < 3 or parcelas > 10:
        print('QUANTIDADE INVÁLIDA')
    else:
        print('Em {}x de R${:.2f} com juros'.format(parcelas, precox))
else:
    final = 0
    print('NÚMERO INVÁLIDO')
print('Valor final da sua compra: R${:.2f}'.format(final))
print('Agradecemos pela preferência!')

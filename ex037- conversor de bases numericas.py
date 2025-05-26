# Escreva um programa que leia um nº inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal   ***{:^20}

titulo = 'CONVERSOR'
print("=" * 29)
print('{:^29}'.format(titulo))
print("=" * 29)
n = int(input('Digite um número: '))
print('-' * 29)
print('[1] binário \n[2] octal \n[3] hexadecimal')
escolha = int(input('Escolha a base de conversão: '))
if escolha == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Número inválido! Tente novamente...')

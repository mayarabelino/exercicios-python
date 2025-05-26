# Faça um programa que leia um nº inteiro e diga se ele é ou não um nº primo
# nº primo só é divisivel por 1 e por ele mesmo

num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')  # coloca a cor verde para os número dividíveis
        tot += 1
    else:
        print('\033[31m', end=' ')  # coloca a cor vermelha para os números não divisíveis
    print(c, end=' ')
print('\n\033[mO número {} foi divisível {} vezes. '.format(num, tot))
if tot == 2:
    print('Ele É PRIMO')
else:
    print('Ele NÃO É PRIMO')



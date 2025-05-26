# Crie um programa que leia dois valores e mostre um menu na tela:
# 1 somar
# 2 multiplicar
# 3 maior
# 4 novos números
# 5 sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso

from time import sleep
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
escolha = 0
while escolha != 5:
    sleep(0.5)
    print('>' * 30)
    print('{:^30}'.format('MENU DE OPÇÕES'))
    print('<' * 30)
    print('[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR NÚMERO\n[4] NOVOS NÚMEROS\n[5] SAIR')
    escolha = int(input('Digite a opção desejada: '))
    if escolha == 1:
        soma = n1 + n2
        print('CALCULANDO...')
        sleep(1)
        print('{} + {} = {}'.format(n1, n2, soma))
    elif escolha == 2:
        multiplica = n1 * n2
        print('CALCULANDO...')
        sleep(1)
        print('{} x {} = {}'.format(n1, n2, multiplica))
    elif escolha == 3:
        if n1 > n2:
            print('MAIOR: {}'.format(n1))
        elif n2 > n1:
            print('MAIOR: {}'.format(n2))
        else:
            print('São IGUAIS')
    elif escolha == 4:
        print('Informe novos valores')
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    elif escolha > 5:
        print('OPÇÃO INVÁLIDA! Tente novamente')
print('SAINDO', end='')
sleep(0.5)
print('. ', end='')
sleep(0.5)
print('. ', end='')
sleep(0.5)
print('.')
print('Fim do programa.')
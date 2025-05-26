# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(* num):
    cont = 0
    maior = 0
    print('*' * 40)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:       # se for o primeiro valor
            maior = valor
        else:               # os demais valores a partir do segundo
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} valores no total.')
    print(f'E o maior valor informado foi {maior}.')
    print('*' * 40)


# Programa principal
maior(8, 3, 4, 9, 1, 5)
maior(3, 4)
maior(4, 6, 1, 2, 0)
maior(7)
maior()
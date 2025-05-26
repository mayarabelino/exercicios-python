# Faça um programa que tenha uma função chamada contador(),
# que receba 3 parâmetros: inicio, fim e passo e realize a contagem.
# Seu programa tem que realizar 3 contagens através da função criada:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada
from time import sleep

def contador(i, f, p):
    if p < 0:
        p = -p
    if p == 0:
        p = 1
    print('=' * 47)
    print(f'A contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.3)
    if i > f:
        for c in range(i, f-1, -p):
            print(c, end=' ')
            sleep(0.3)
    print('Fim!')


#Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 47)
print('Agora é sua vez de personalizar sua contagem...')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)


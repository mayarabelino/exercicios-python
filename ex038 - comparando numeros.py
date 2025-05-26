# Escreva um programa que leia dois nº inteiro e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Ou, Não existe valor maior, os dois são iguais

from time import sleep
n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
print('\033[31mCALCULANDO, AGUARDE...\033[m')
sleep(2)
if n1 > n2:
    print('O primeiro valor é maior')
elif n2 > n1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, ambos são iguais')

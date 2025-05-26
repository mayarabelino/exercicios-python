# Crie um programa que leia um nº real qualquer pelo teclado e mostre na tela sua porção inteira
# ex: o nº 6.127 tem a parte inteira 6
import math
n = float(input('Digite um número: '))
print('A parte inteira do número {} é {}'.format(n, int(n)))
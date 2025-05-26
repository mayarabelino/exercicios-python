# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input('Informe qual ano você quer analisar. Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print('{} é um ano bissexto.'.format(ano))
else:
    print('{} não é um ano bissexto.'.format(ano))

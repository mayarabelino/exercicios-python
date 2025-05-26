# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar
# Se é a hora de se alistar
# Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
# date.today().year

from datetime import date
print('-*-' * 14)
titulo = 'ALISTAMENTO MILITAR'
print(titulo.center(42))
print('-*-' * 14)
anoNasc = int(input('Informe o ano de nascimento: '))
anoAtual = date.today().year  #informa o ano atual
idade = anoAtual - anoNasc
print('Você está com {} anos'.format(idade))
if idade < 18:
    alista = 18 - idade
    print('Ainda não está na hora, falta {} ano(s)'.format(alista))
elif idade == 18:
    print('\033[32mÉ hora de se alistar! VAMOS LÁ!\033[m')
else:
    alista = idade - 18
    print('\033[31mJá passou da hora, o prazo foi a {} ano(s)\033[m'.format(alista))



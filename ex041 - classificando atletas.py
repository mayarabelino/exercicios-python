# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM, Até 14 anos: INFANTIL, Até 19 anos: JUNIOR, Até 25 anos: Senior, Acima: MASTER

from datetime import date
tituto = 'Confederação Nacional de Natação'
print('<' * 40)
print(tituto.center(40))
print('>' * 40)
ano = int(input('Digite o ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Idade: {} anos\nCategoria: '.format(idade), end='')
if idade <= 9:
    print('MIRIM')
elif idade <=14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
atual = date.today().year
smaior = 0
smenor = 0
for c in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    idade = atual - ano
    if idade >= 18:
        smaior += 1
    else:
        smenor += 1
print('Ao todos {} pessoas não atingiram a maioridade ainda e {} pessoas já são maiores'.format(smenor, smaior))



# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o nº escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
aleatorio = randint(0,5)
n = int(input('Qual é o número entre 0 e 5 que o computador está pensando? '))
print('PROCESSANDO...')
sleep(2)  # O programa "espera" por 2 segundos
if n == aleatorio:
    print('Você venceu!')
else:
    print('Você perdeu! O número correto é {}'.format(aleatorio))


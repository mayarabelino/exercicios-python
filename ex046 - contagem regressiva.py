# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 seg entre eles

import emoji
from time import sleep
print('{:*^33}'.format(' CONTAGEM REGRESSIVA '))
for c in range (10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize(':fireworks:') * 5, 'FELIZ ANO NOVO',emoji.emojize(':fireworks:') * 5)
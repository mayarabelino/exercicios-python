# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from operator import itemgetter
from random import randint
from time import sleep

ranking = []

jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f' O {k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)      # ranking virou uma lista e não mais um dicionário
print('=' * 30)
print('Ranking dos jogadores:')
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(0.5)
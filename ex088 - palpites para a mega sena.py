# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

import random
from time import sleep

print('=' * 40)
print(f'{'JOGO DA MEGA SENA':^40}')
print('=' * 40)
qntjogos = int(input('Quantos jogos você quer? '))
print(f'{f'>>>>>>>>> SORTEANDO {qntjogos} JOGOS <<<<<<<<<':^40}')
for c in range(0,qntjogos):
    sorteados = random.sample(range(1,61), 6)       # sorteia 6 nº entre 1 e 60
    sorteados.sort()
    sleep(0.7)
    print(f'Jogo {c+1}: {sorteados}')

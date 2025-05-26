# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gols = []
soma = 0

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
if partidas > 0:
    for i in range(1,partidas+1):
        gol = int(input(f' Quantos gols na {i}ª partida? '))
        gols.append(gol)
        soma += gol
jogador['gols'] = gols[:]
jogador['total'] = soma
# jogador['total'] = sum(gols)  -> é outra forma de fazer
print('>' * 40)
print(jogador)
print('>' * 40)

for k, v in jogador.items():
    print(f' > {k}: {v}')
print('>' * 40)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f' Na {i+1}ª partida, fez {g} gols.')
print(f'Foi um total de {jogador['total']} gols.')

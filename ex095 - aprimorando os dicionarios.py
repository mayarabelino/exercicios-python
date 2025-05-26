# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# Aprimore o DESAFIO 093 para que ele funciona com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador

jogador = {}
gols = []
lista = []
resp = 'S'

while resp == 'S':
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    gols.clear()
    for i in range(1, partidas+1):
        gols.append(int(input(f'  Quantos gols na {i}ª partida: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    lista.append(jogador.copy())

    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Resposta inválida. Digite novamente [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        print('FINALIZANDO...')

print('=' * 60)
print(f'{'cod':<4}{'Nome':<15}{'Gols':<15}{'Total'}')
print('-' * 50)
for k, v in enumerate(lista):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 p/ parar) '))
    if busca == 999:
        break
    if busca >=len(lista):
        print(f'Erro! Não existe jogador com código {busca}!')
    else:
        print(f'Levantamento do jogador {lista[busca]["nome"]}:')
        for i, g in enumerate(lista[busca]['gols']):
            print(f'   No jogo {i+1} fez {g} gols.')
print('-' * 50)
print('ENCERRANDO...')
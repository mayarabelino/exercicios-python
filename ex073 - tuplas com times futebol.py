# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela de Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# A) Apenas os 5 primeiros colocados
# B) Os ultimos 4 colocados
# C) Uma lista com os times em ordem alfabética
# D) Em que posição na tabela está o time Flamengo

tabelaBrasileiro = ('Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Bahia', 'Internacional', 'Cruzeiro',
                    'Atlético MG', 'Vasco', 'Criciúma', 'Grêmio', 'Red Bull Bragantino', 'Juventude', 'Fluminense',
                    'Corinthians', 'Atlético PR', 'Vitória', 'Cuiabá', 'Atlético GO')
print('Tabela de times do Brasileirão:')
for pos, t in enumerate(tabelaBrasileiro):
    print(f'{pos+1:2}º.......... {t}')
print('>' * 100)
print(f'Os cinco primeiros colocados: {tabelaBrasileiro[0:5]}')
print('>' * 100)
print(f'Os últimos 4 colocados: {tabelaBrasileiro[-4:]}')
print('>' * 100)
print(f'Times em ordem alfabética: {sorted(tabelaBrasileiro)}')
print('>' * 100)
print(f'O Flamengo está na {tabelaBrasileiro.index('Flamengo')+1}ª posição')

# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um
# e permita que o usuário possa mostrar as notas de cada aluno individualmente
from time import sleep

alunos = []
resp = 'S'

while resp == 'S':
    nome = str(input('Nome do(a) aluno(a): '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], media])

    resp = str(input('Deseja continuar? [S/N]\n')).strip().upper()[0]
    while resp != 'N' and resp != 'S':
        resp = str(input('RESPOSTA INVÁLIDA! Digite novamente: [S/N]\n')).strip().upper()[0]
    if resp == 'N':
        print('Carregando', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.', end='')
        sleep(0.5)
        print('.')
print('=' * 30)
print(f'{'Nº':<4}{'Nome':<10}{'Média':>8}')
print('=' * 30)
for c in range(0,len(alunos)):
    print(f'{c:<4}{alunos[c][0]:<10}{alunos[c][2]:>8.1f}')

while True:
    print('><' * 15)
    escolha = int(input('Mostrar as notas de qual aluno? (999 para interromper):\n'))
    if escolha == 999:
        print('FINALIZANDO...')
        break
    if escolha <= len(alunos) - 1:
        print(f'As notas do {alunos[escolha][0]} são: {alunos[escolha][1]}')

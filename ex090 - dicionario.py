# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

aluno = {}

aluno['nome'] = str(input('Nome do aluno: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-' * 20)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["média"]}')
print(f'Situação: {aluno["situação"]}')

print('=' * 20)
for k, v in aluno.items():
    print(f'{k}: {v}')
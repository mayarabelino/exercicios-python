# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
# A) quantas pessoas foram cadastradas
# B) a média de idade do grupo
# C) uma lista com todas as mulheres
# D) uma lista com todas as pessoas com idade acima da média

pessoa = {}
lista = []
resp = 'S'
soma = 0

while resp == 'S':
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo [F/M]: ')).strip().upper()[0]
    while pessoa['sexo'] != 'F' and pessoa['sexo'] != 'M':
        pessoa['sexo'] = str(input('INVÁLIDO. Digite novamente [F/M] ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())
    soma += pessoa['idade']
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp != 'S' and resp != 'N':
        resp = str(input('Resposta inválida. Responda S ou N.\nQuer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        print('Finalizando...')

print(f'Quantidade total de pessoas cadastradas: {len(lista)}')
print(f'Média de idade do grupo: {soma / len(lista):.2f} anos')
print(f'Mulheres cadastradas: ', end='')
for p in lista:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
print(f'Pessoas com idade acima da média: ')
for p in lista:
    if p['idade'] >= (soma / len(lista)):
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print('\n')

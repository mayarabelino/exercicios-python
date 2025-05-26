# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final mostre:
# A) Quantas pessoas foram cadastradas
# B) Uma listagem com as pessoas mais pesadas
# C) Uma listagem com as pessoas mais leves

from time import sleep
pessoa = []
dados = []
resp = 'S'
# soma = 0
maior = menor =  0

while resp == 'S':
    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    dados.append(pessoa[:])
    pessoa.clear()
#   soma +=1

    resp = str(input('Deseja continuar: (S/N)\n')).strip().upper()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Resposta INVÁLIDA! Digite novamente (S/N)\n')).strip().upper()[0]
    if resp == 'N':
        print('FINALIZANDO...')
        sleep(1)

    for i, p in enumerate(dados):
        if i == 0:
            maior = p[1]
            menor = p[1]
        else:
            if p[1] > maior:
                maior = p[1]
            if p[1] < menor:
                menor = p[1]

print('=' * 40)
print(f'Foram cadastrados ao todo {len(dados)} pessoas.')     # Ao invés do contador 'soma', pode ser utilizado len()
print(f'O maior peso é {maior}kg de: ', end='')
for p in dados:
    if p[1] == maior:
        print(f'{p[0]}...', end='')
print(f'\nO menor peso é {menor}kg de: ', end='')
for p in dados:
    if p[1] == menor:
        print(f'{p[0]}...', end='')

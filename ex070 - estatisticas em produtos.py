# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar. No final mostre:
# Qual é o total gasto na compra
# Quantos produtos custam mais de R$ 1000
# Qual é o nome do produto mais barato

total = 0
maisMil = 0
baratoNome = ''
barato = 0
cont = 0
print('<' * 30)
print(F'{'L O J A   + Q D + ':^30}')
print('>' * 30)
while True:
    nomeP = str(input('Insira o nome do produto: '))
    precoP = float(input('Insira o preço do produto: R$ '))
    cont += 1
    total += precoP
    if precoP > 1000:
        maisMil += 1
    if cont == 1 or precoP < barato:
        barato = precoP
        baratoNome = nomeP
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if escolha == 'N':
        break
    print('<>' * 15)
print(f'Total da sua compra: R${total:.2f}')
print(f'Quantidade de produtos acima de R$1000,00: {maisMil}')
print(f'O produto mais barato: {baratoNome}')
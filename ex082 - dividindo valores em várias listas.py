# Crie um programa que vai ler vários nº e colocar em uma lista
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os impares digitados, respectivamente
# Ao final, mostre o conteúdos das 3 listas geradas

valores = []
pares = []
impares = []
resposta = 'S'

while resposta == 'S':
    valores.append(int(input('Digite um número: ')))
    resposta = str(input('Deseja continuar digitando? (S/N)\n')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida. Digite novamente: (S/N)\n')).strip().upper()[0]
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('*-' * 30, end='')
print('*')
print(f'Lista completa: {valores}')
print(f'Lista dos números pares: {pares}')
print(f'Lista dos número ímpares: {impares}')
print('*-' * 30, end='')
print('*')

# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário
# O programa será interrompido quando o nº solicitado for negativo


while True:
    i = 1
    print('-' * 35)
    n = int(input('Qual número deseja ver a tabuada? '))
    print('-' * 35)
    if n < 0:
        break
    while i <= 10:
        res = n * i
        print(f'{n} x {i:2} = {res:2}')
        i += 1
print('Fim do Programa!')

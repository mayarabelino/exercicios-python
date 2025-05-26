# Faça um programa que jogue par ou impar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
aleatorio = randint(0,10)
soma = 0
cont = 0
while True:
    print('-' * 35)
    n = int(input('Escolha um número de 0 a 10: '))
    print('-' * 35)
    soma = n + aleatorio
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? (P/I) ')).strip().upper()
    print('-' * 35)
    if soma % 2 == 0:
        if escolha == 'P':
            print(f'Você venceu! O computador escolheu o nº {aleatorio} e a soma entre eles foi {soma}')
            cont += 1
        elif escolha == 'I':
            print(f'Você perdeu... O computador escolheu {aleatorio} e a soma entre eles foi {soma}')
            break
    if soma % 2 != 0:
        if escolha == 'I':
            print(f'Você venceu! O computador escolheu o nº {aleatorio} e a soma entre eles foi {soma}')
            cont += 1
        elif escolha == 'P':
            print(f'Você perdeu... O computador escolheu {aleatorio} e a soma entre eles foi {soma}')
            break
if cont > 0:
    print(f'Você ganhou {cont} jogos consecutivos. Parabéns!')
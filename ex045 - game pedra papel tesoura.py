# Crie um programa que faça o computador jogar JOKENPÔ com você
# 🖐️ papel
# 👊 pedra
# ✌️ tesoura

from time import sleep
from random import choice
e1 = '🖐️'
e2 = '👊'
e3 = '✌️'
lista = [e1, e2, e3]
escolhidopc = choice(lista)
print('<' * 20)
titulo = 'VAMOS JOGAR'
print(titulo.center(20))
print('>' * 20)
print('[1] 👊 (pedra)\n[2] 🖐️ (papel)\n[3] ✌️ (tesoura)')
escolha = int(input('Escolha uma opção: '))
print('-' * 20)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('-' * 20)
print('Computador escolheu {}'.format(escolhidopc))
print('-' * 20)
if escolha == 1:    #escolhendo pedra
    if escolhidopc == e1:
        print('VOCÊ PERDEU...')
    elif escolhidopc == e2:
        print('EMPATOU')
    else:
        print('VOCÊ GANHOU!')
elif escolha == 2:      #escolhendo papel
    if escolhidopc == e1:
        print('EMPATOU')
    elif escolhidopc == e2:
        print('VOCÊ GANHOU!')
    else:
        print('VOCÊ PERDEU...')
elif escolha == 3:      #escolhendo tesoura
    if escolhidopc == e1:
        print('VOCÊ GANHOU!')
    elif escolhidopc == e2:
        print('VOCÊ PERDEU...')
    else:
        print('EMPATE')
else:
    print('NÚMERO INVÁLIDO')








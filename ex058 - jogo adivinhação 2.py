# Melhore o jogo do ex028 onde o pc vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer

from random import randint
aleatorio = randint(0,10)
soma = 0
print('*-*-*-*-*-*-* VAMOS JOGAR *-*-*-*-*-*-*')
num = int(input('Qual número entre 0 e 10 estou pensando? '))
while num != aleatorio:
    if num < aleatorio:
        num = int(input('É mais... Tente novamente: '))
    elif num > aleatorio:
        num = int(input('É menos... Tente novamente: '))
    soma += 1
if soma == 0:
    print('Parabéns! Você acertou de primeira!')
else:
    print('Parabéns! Você acertou na {}ª tentativa.'.format(soma+1))
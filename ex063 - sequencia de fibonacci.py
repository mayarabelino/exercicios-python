# Escreva um programa que leia um número n inteiro qualquer e
# mostre na tela os n primeiros elementos de uma sequência de Fibonacci
# Ex: 0 > 1 > 1 > 2 > 3 > 5 > 8

n = int(input('Informe a quantidade de elementos: '))
print('Abaixo a sequência de Fibonacci com {} elementos'.format(n))
t1 = 0      # valores iniciais
t2 = 1      # valores iniciais
print('{} > {}'.format(t1, t2), end='')
cont = 3    # já foi mostrado o primeiro e segundo termo (t1 e t2)
while cont <= n:
    t3 = t1 + t2
    print(' > {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' > FIM')

n = int(input('Digite um número para calcular seu FATORIAL: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')    # coloca 'x' enquanto c > 1 e coloca '=' quando c for 1
    f *= c      # f = f * c
    c -= 1
print('{}'.format(f))
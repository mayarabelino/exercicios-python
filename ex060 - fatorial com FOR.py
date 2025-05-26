print('!!! CALCULANDO FATORIAL !!!')
num = int(input('Digite um número: '))
f = 1       # como estamos multiplicando, precisa iniciar com 1, se não a resultado ficará zeo
c = 1
for c in range(num, 1, -1):
    f = f * c
print('{}! = {}'.format(num, f))
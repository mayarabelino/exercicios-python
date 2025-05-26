resposta = 'S'

print('-' * 29)
print('{:^29}'.format('TERMOS DE UMA PA'))
print('-' * 29)

while resposta == 'S':
    i = 0
    t1 = int(input('Primeiro termo: '))
    r = int(input('Razão: '))
    qn = int(input('Quantos termos gostaria de mostrar: '))
    tn = t1 + (qn - 1) * r
    while i < tn:
        print(t1, end=' > ')
        t = t1 + r
        t1 = t
        i += r
    print('FIM')
    resposta = str(input('Deseja continuar? (S/N) ')).strip().upper()
print('FIM')
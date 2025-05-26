termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
i = 1
t = termo1
total = 0       # total de termos que será mostrado
mais = 10       # quantidade que será mostrado a mais (programa começa com 10 termos)
while mais != 0:
    total = total + mais
    while i <= total:
        print(t, end=' > ')
        t = t + razao
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostra a mais? '))
print('Progressão finalizada com {} termos mostrado.'.format(total))
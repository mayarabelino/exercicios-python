# Refaça o ex051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
# Tn = T1 + (n-1) * razao - FORMULA

print('-' * 29)
print('{:^29}'.format('10 TERMOS DE UMA PA'))
print('-' * 29)

t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 0
t = t1
while i < 10:
    print(t, end=' > ')
    t = t + r
    i += 1
print('FIM')
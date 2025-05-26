# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética).
# No final, mostre os 10 primeiros termos dessa progressão

print('-' * 29)
print('{:^29}'.format('10 TERMOS DE UMA PA'))
print('-' * 29)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10-1) * razao      #formula do enesimo nº de uma PA
for c in range(primeiro, decimo + razao, razao):
    print(c, end=' > ')
print('ACABOU')


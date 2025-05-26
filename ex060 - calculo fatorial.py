# Faça um programa que leia um número qualquer e mostre o seu fatorial
# Exemplo: 5! = 5x4x3x2x1 = 120

print('*' * 30)
print('{:^30}'.format('CALCULANDO FATORIAL'))
print('*' * 30)

i = 1
soma = 0
num = int(input('Digite um número: '))
f1 = num
f2 = f1 - 1
while i < num:
    f3 = f1 * f2
    f1 = f3
    f2 -= 1
    i += 1
print('*' * 30)
print('{}! = {}'.format(num, f3))
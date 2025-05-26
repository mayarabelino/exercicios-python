# Desenvolva um programa que leia 6 nº inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o

s = 0
for c in range(1,7):
    num = int(input('Digite o {}º número: '.format(c)))
    if num % 2 == 0:
        s += num
print('A soma entre os números pares é {}'.format(s))

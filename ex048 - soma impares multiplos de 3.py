# Faça um programa que calcule a soma entre todos os todos os nº impares que são multiplos de 3 e
# que se encontrem no intervalo de 1 até 500

s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
print('A soma dos números ímpares e múltiplos de 3 entre 1 e 500 é {}'.format(s))



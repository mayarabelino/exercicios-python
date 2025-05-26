# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados
# B) A soma dos valores da terceita coluna
# C) O maior valor da segunda linha

somapar = 0
somacoluna3 = 0
maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            somacoluna3 += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            else:
                if matriz[l][c] > maior:
                    maior = matriz[l][c]

print('=' * 50)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('=' * 50)
print(f'A soma de todos os valores pares é {somapar}')
print(f'A soma dos valores a 3ª coluna é {somacoluna3}')
print(f'O maior valor da 2ª linha é {maior}')



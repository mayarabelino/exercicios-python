# Crie um programa onde o usuário possa digitar 7 valores numéricos
# e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
# No final, mostre os valores pares e impares em ordem crescente

valores = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite o {c}º número: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

print('=' * 50)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')
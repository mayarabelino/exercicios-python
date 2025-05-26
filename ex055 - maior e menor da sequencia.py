# Faça um programa que leia o peso de 5 pessoas.
# No final, mostre qual foi o maior e o menor peso lidos

maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa em kg: '.format(p)))
    if p == 1:      # o primeiro peso, como não tem comparativo, vai ser o maior e também vai ser o menor informado
        maior = peso
        menor = peso
    else:           # cada vez que um peso é lido, vai verificar se é maior ou menor que o primeiro
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso é {}kg'.format(menor))



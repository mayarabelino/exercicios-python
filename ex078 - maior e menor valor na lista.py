# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

valores = []
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input(f'Digite o valor da {c+1}ª posição: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'Lista: {valores}')
print(f'O maior valor é {maior}, está na posição: ', end='')
for i, v in enumerate(valores):     # i é a posição do elemento da lista / v é o valor correspondente a essa posição
    if v == maior:
        print(f'{i+1}...', end='')          # i+1 devido ao c+1 nas posições iniciais
print()         # somente para quebrar a linha

print(f'O menor valor é {menor}, está na posição: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i+1}...', end='')
print()         # somente para quebrar a linha
#print(f'O maior valor da lista é {max(valores)} e está na {valores.index(max(valores))+1}ª posição')
#print(f'O menor valor é {min(valores)} e está na {valores.index(min(valores))+1}ª posição')

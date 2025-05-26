# Crie um programa que vai ler vários nº e colocar em uma lista.
# Depois disso mostre:
# A) Quantos nº foram digitados
# B) A lista de valores, ordenada de forma decrescente
# C) Se o valor 5 foi digitado e está ou não na lista

valores = []
resposta = 'S'

while resposta == 'S':
    valores.append(int(input('Digite um valor: ')))
    resposta = str(input('Deseja continuar digitando? (S/N)\n')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida! Deseja continuar digitando? (S/N)\n')).strip().upper()[0]

print(f'Foram digitados {len(valores)} números.')
valores.sort(reverse=True)
print(f'Essa é a lista em ordem decrescente: {valores}')
if valores.count(5) != 0:
    print(f'O número 5 foi digitado e aparece {valores.count(5)} vez(es) na lista, na(s) posição(ões) ', end='')
    for i, v in enumerate(valores):
        if v == 5:
            print(f'{i}...', end='')
else:
    print('O número 5 NÃO foi digitado e NÃO aparece na lista')

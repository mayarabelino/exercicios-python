# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o nº já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
while True:         # loop infinito, só para com o break
    n = int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado!')
    else:
        print('Esse valor já foi adicionado. Tente outro!')
    resp = str(input('Deseja continuar digitando? (S/N)\n')).strip().upper()[0]
    if resp in 'N':
        break

valores.sort()
print('-' * 50)
print(f'Lista em ordem crescente: {valores}')
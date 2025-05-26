# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o nº já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores = []
resposta = 'S'
aux = []
while resposta == 'S':
    valores.append(int(input('Digite um valor: ')))
    for i, v in enumerate(valores):
        if i == 0:
            print('Valor adicionado...')
            aux.append(v)
        else:
            if v in aux:
                valores.append(int(input('Esse valor já foi adicionado. Digite outro: ')))
            else:
                print('Valor adicionado...')
                aux.append(v)
    resposta = str(input('Deseja continuar digitando? (S/N)\n')).strip().upper()[0]
    while resposta != 'S' and resposta != 'N':
        resposta = str(input('Resposta inválida! Deseja continuar digitando? (S/N)\n')).strip().upper()[0]



valores.sort()
print(valores)
print(aux)
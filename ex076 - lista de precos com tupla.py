# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequencia.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular
# Ex Saída: Lápis......................R$ 1.75

produtos = ('Caderno', 20.9,
            'Lápis', 2.0,
            'Caneta', 3.55,
            'Borracha', 2.99,
            'Mochila', 99.9,
            'Cola', 3.2,
            'Agenda', 32.5)
print('=' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('=' * 40)
for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
        print(f'{produtos[posicao]:.<30}', end='')
    else:
        print(f'R${produtos[posicao]:>6.2f}')
print('=' * 40)
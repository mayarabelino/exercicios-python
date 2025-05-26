# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento)
# e mostre a área do terreno

def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}x{comp} é de {a}m².')


#Programa Principal
print(f'{'Controle de Terrenos':^24}')
print('-' * 24)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)


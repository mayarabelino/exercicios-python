# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m²
al = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = al * lar
t = area / 2
print('A área dessa parede é de {:.2f}m².\nA quantidade de tinta necessária é de {:.2f} litros.'.format(area, t))

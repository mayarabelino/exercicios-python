# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo,
# calcule e mostra o comprimento da hipotenusa
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(h))
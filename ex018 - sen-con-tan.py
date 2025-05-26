# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
import math
an = float(input('Digite um ângulo: '))
# o calculo do seno/cosseno/tangente é com a medida em radianos, por isso precisa ser convertido
sen = math.sin(math.radians(an))
print('O ângulo de {} tem o seno de {:.2f}'.format(an, sen))
cos = math.cos(math.radians(an))
print('O cosseno é {:.2f}'.format(cos))
tan = math.tan(math.radians(an))
print('E a tangente é {:.2f}'.format(tan))

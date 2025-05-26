# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo

r1 = float(input('Qual comprimeiro da 1ª reta? '))
r2 = float(input('Qual comprimento da 2ª reta? '))
r3 = float(input('Qual comprimento da 3ª reta? '))
if (r1 + r2 > r3) and (r2 + r3 > r1) and (r1 + r3 > r2):
    print('Essas retas podem formar um triângulo.')
else:
    print('Essas retas não formam um triângulo.')

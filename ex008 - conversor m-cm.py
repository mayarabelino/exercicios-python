# Escreva um programa que leia um valor em metros e o exiba convertido em centímetro e milímetros
m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('O valor em centímetros desse número é: {:.2f}cm.\nE o valor em milímetros é: {:.2f}mm.'.format(cm, mm))
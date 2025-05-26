# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
# No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

soma = 0
contador = 0
num = 0
print('>>>>> O programa vai somar quantos números você quiser, e para parar digite "999" <<<<<')
num = int(input('Digite um número: '))
while num != 999:
    soma += num
    contador += 1
    num = int(input('Digite um número: '))
print('Encerrado!')
print('Você digitou {} números, e a soma desses números é {}'.format(contador, soma))
# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lido.
# O programa deve perguntar ao usuario se ele quer ou não continuar a digitar valores

from time import sleep
resposta = 'S'
soma = 0
cont = 0
maior = 0
menor = 0
while resposta == 'S':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resposta = str(input('Deseja continuar digitando? (S/N) ')).strip().upper()
print('FINALIZADO')
print('Aguarde enquanto calculamos para você...')
sleep(2)
print('===' * 22)
media = soma / cont
print('Foram digitados {} números e a média entre esses números é {:.2f}'.format(cont, media))
print('MAIOR valor: {} \nMENOR valor: {}'.format(maior, menor))
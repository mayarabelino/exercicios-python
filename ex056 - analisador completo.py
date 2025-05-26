# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa mostre:
# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos

velho = ''
maior = 0
totalIdade = 0
somaMulheres = 0
for p in range(1,5):
    print('*-*- {}ª PESSOA -*-*'.format(p))
    nome = str(input('Digite seu nome: ')).strip()
    idade = int(input('Digite sua idade: '))
    totalIdade += idade
    sexo = str(input('Digite seu sexo (F/M): ')).strip().upper()
    if sexo == 'F':
        if idade < 20:
            somaMulheres += 1
    else:
        if idade > maior:
            maior = idade
            velho = nome

media = totalIdade / p      # pega todas as idades somadas e divide pela quantidade de pessoas
print('A média de idade do grupo é {} anos'.format(int(media)))
print('Ao todo {} mulher(es) tem menos de 20 ano(s)'.format(somaMulheres))
print('O homem mais velho é {} e tem {} anos'.format(velho, maior))


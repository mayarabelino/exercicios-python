# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

nome = str(input('Digite seu nome completo: ')).strip()
dividido = nome.split()
print('Primeiro nome: {}'.format(dividido[0]))
print('último nome: {}'.format(dividido[len(dividido)-1]))

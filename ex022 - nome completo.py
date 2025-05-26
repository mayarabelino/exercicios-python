# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as minusculas
# Quantas letras no total (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
print('Com letras maiusculas: {}'.format(nome.upper()))
print('Com letras minusculas: {}'.format(nome.lower()))
# dividido = nome.split()
# junto = ''.join(dividido)
# print('Total de letras: {}'.format(len(junto)))
print('Total de letras: {}'.format(len(nome) - nome.count(' ')))
# print('Primeiro nome tem {} letras'.format(len(dividido[0])))
print('Primeiro nome tem {} letras'.format(nome.find(' ')))


# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()[0]     # o [0] significa pegar só a primeira letra
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Informação incorreta. Digite novamente: ')).strip().upper()
if sexo == 'F':
    print('Sexo FEMININO registrado.')
if sexo == 'M':
    print('Sexo MASCULINO registrado.')



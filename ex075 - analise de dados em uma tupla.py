# Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
# No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares

num = (int(input('Digite o 1º número: ')),
       int(input('Digite o 2º número: ')),
       int(input('Digite o 3º número: ')),
       int(input('Digite o 4º número: ')))
print(f'Você digitou os valores: {num}')

print(f'O número 9 aparece {num.count(9)} vezes')

if 3 in num:
       print(f'O número 3 é a {num.index(3)+1}ª posição')
else:
       print('O valor 3 não foi digitado')

print(f'Os valores pares digitados foram ', end='')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')

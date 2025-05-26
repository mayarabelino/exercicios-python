# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra 'a'
# Em que posição aparece a primeira vez
# Em que posição aparece a ultima vez

frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra "a" aparece {} vezes'.format(frase.count('a')))
print('A primeira vez aparece na posição {}'.format(frase.find('a')+1))
print('A última vez aparece na posição {}'.format(frase.rfind('a')+1))
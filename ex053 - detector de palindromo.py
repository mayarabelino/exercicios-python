# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
# palindromo é a frase que mesmo virando ao contrário continua igual
# ex: APOS A SOPA

frase = str(input('Digite uma frase: ')).strip().upper()
dividido = frase.split()
junto = ''.join(dividido)
fraseInvertida = ''
# fraseInvertida = junto[::-1]    -> essa seria uma forma resumida para inverter a frase, sem precisar do FOR
for c in range(len(junto) -1, -1, -1):
    fraseInvertida += junto[c]
print('O inverso da frase {} é {}'.format(junto, fraseInvertida))
if fraseInvertida == junto:
    print('Essa frase é um PALÍNDROMO')
else:
    print('Essa frase NÃO é um PALÍNDROMO')


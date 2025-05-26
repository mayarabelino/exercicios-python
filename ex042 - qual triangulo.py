# Refaça o ex035 dos triângulos, acrescentando o recuso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

print('{}Digite abaixo o comprimento de cada reta{}'.format('\033[1;35;40m', '\033[m '))
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
print('Essas retas formam um triângulo? ')
if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('{}SIM!{} E esse é um triângulo'.format('\033[32m','\033[m'), end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('{}NÃO!{}'.format('\033[31m', '\033[m'))



# Refaça o ex009, mostrando a tabuada de um nº que o usuario escolher, só que agora utilizando o laço for

num = int(input('Digite um número inteiro: '))
print('-=' * 15)
print('{:^30}'.format('TABUADA'))
print('-=' * 15)
for c in range(1,11):
    print('{} x {:2} = {:2}'.format(num, c, num*c))
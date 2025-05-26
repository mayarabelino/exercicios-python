# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Abaixo de 5.0 REPROVADO, entre 5.0 e 6.9 RECUPERAÇÃO, acima de 7.0 APROVADO

cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('-'*38)
titulo = 'BOLETIM ESCOLAR'
print(titulo.center(38))
print('-'*38)
if media < 5:
    print('Sua média foi {:.1f}, está {}REPROVADO{}'.format(media, cores['vermelho'], cores['limpa']))
elif media >= 7:
    print('Sua média foi {:.1f}, está {}APROVADO{}!\n{}PARABÉNS{}!'
          .format(media, cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
else:
    print('Sua média foi {}, está em RECUPERAÇÃO'.format(media))



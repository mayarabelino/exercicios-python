# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota do(a) aluno(a) {}: '.format(nome)))
n2 = float(input('Digite a segunda nota do(a) aluno(a) {}:'.format(nome)))
media = (n1+n2)/2
print('A média de {} é: {:.2f}'.format(nome, media))

# Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro
# e mostre uma mensagem com tamanho adaptável.
#Ex: escreva('Olá Mundo')
# Saída:
# ~~~~~~~~~
# Olá Mundo
# ~~~~~~~~~

def escreva(txt):
    tamanho = len(txt) + 2
    print('~' * tamanho)
    print(f' {txt} ')
    print('~' * tamanho)


#Programa Principal
escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')
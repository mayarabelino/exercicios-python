# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual será o valor a ser sacado (nº inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues
# obs: considere que o caixa possui cédulas de R$ 50, 20, 10 e 1

valor = int(input('Digite o valor para sacar: R$ '))
total = valor
cedula = 50         # para esse programa é a maior cédula
qntcedula = 0
while True:
    if total >= cedula:
        total -= cedula         # vai diminuir o valor da cédula do total
        qntcedula += 1          # vai somar 1 a quantidade de cédulas utilizadas do mesmo valor
    else:
        if qntcedula > 0:
            print(f'> {qntcedula} cédulas de R$ {cedula}')
        if cedula == 50:        # se a cédula ainda for 50 e o total já for menor que o valor da cédula
            cedula = 20
        elif cedula == 20:      # se a cédula ainda for 20 e o total já for menor que o valor da cédula
            cedula = 10
        elif cedula == 10:      # se a cédula ainda for 10 e o total já for menor que o valor da cédula
            cedula = 1
        qntcedula = 0           # zerando a quantidade de cédulas para poder calcular com os próximos valores de cédulas
        if total == 0:
            break
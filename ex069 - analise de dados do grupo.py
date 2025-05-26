# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# Quantas pessoas tem mais de 18 anos
# Quantos homens foram cadastrados
# Quantas mulheres tem menos de 20 anos

somaMais18 = 0
somaHomens = 0
somaMulheres = 0
while True:
    print('*' * 30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: (F/M) ')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        print('Informação inválida')
        sexo = str(input('Sexo: (F/M) ')).strip().upper()[0]
    print('*' * 30)
    if idade > 18:
        somaMais18 += 1
    if sexo == 'M':
        somaHomens += 1
    if sexo == 'F' and idade < 20:
        somaMulheres += 1
    escolha = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    while escolha != 'S' and escolha != 'N':
        print('Informação inválida')
        escolha = str(input('Deseja continuar? (S/N) ')).strip().upper()[0]
    if escolha == 'N':
        break
print('=' * 30)
print(f'Pessoas com mais de 18 anos: {somaMais18}')
print(f'Total de homens cadastrados: {somaHomens}')
print(f'Total de mulher com menos de 20 anos: {somaMulheres}')
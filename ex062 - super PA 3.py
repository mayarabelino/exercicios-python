# Melhore o ex061, perguntando para o usuario se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
# Tn = T1 + (n-1) * razao - FORMULA

t1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
i = 0
taux = t1
while i < 10:
    print(t1, end=' > ')
    t = t1 + r
    t1 = t
    i += 1
print('FIM')
resposta = int(input('Gostaria de mostrar mais termos? Quantos: '))
soma = resposta
while resposta != 0:
    i = 0
    t1 = taux
    tn = t1 + ((10 + soma) - 1) * r
    while i < tn:
        print(t1, end=' > ')
        t = t1 + r
        t1 = t
        i += r
    print('FIM')
    resposta = int(input('Gostaria de mostrar mais termos? Quantos: '))
    soma += resposta
print('FIM')
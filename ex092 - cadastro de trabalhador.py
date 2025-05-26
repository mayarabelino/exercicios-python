# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário
# Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar
# OBS: considerar 35 anos de contribuição para aposentadoria

cadastro = {}
from datetime import datetime
cadastro['nome'] = str(input('Nome: '))
anonasc = int(input('Ano de Nascimento: '))
idade = datetime.now().year - anonasc
cadastro['idade'] = idade
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = (cadastro['contratação'] + 35) - anonasc

print('=' * 30)
for k, v in cadastro.items():
    print(f' > {k}: {v}')

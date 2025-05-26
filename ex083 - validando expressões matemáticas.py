# Crie um programa onde o usuário digite uma expressão matemática qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta

# OBS.: toda string(str) é uma lista

expressao = str(input('Digite uma expressão matemática que utilize parênteses: '))
pilha = []
for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:      # verifica se já possui algum elemento na lista
            pilha.pop()         # remove o último elemento da lista
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está incorreta!')

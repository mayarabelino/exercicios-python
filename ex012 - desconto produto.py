#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
p = float(input("Qual preço desse produto? R$"))
pd = p - (p * 0.05)
# outra opção para 0,05 = 10*5/100
print('O preço com 5% desconto é de R${:.2f}'. format(pd))

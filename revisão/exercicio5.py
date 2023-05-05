"""As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem
compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e
escreva o custo total da compra"""

compra = int(input("Informe a quantidade de maças que deseja comprar: "))

if compra < 12:
    valor = compra * 1.30
    print(valor)
else:
    preco = compra * 1.00
    print(preco)

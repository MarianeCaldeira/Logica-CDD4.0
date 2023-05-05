"""Faça um algoritmo que receba 4 números e realize a soma deles e a média entre eles.
E mostre os resultados"""

n1 = float(input("Informe o primeiro: "))
n2 = float(input("Informe o segundo número: "))
n3 = float(input("Informe o terceiro número: "))
n4 = float(input("Informe o quarto número: "))

soma = n1 + n2 + n3 + n4
media = soma / 4
print("\nTotal da soma dos números:", soma)
print("Média aritmétrica:", media)

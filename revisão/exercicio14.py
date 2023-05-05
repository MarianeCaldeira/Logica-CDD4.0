"""Usando FOR, faça um algoritmo que receba 4 números e realize a soma deles e a média entre eles.
E mostre os resultados"""

numeros = []
for x in range(4):
    numeros.append(int(input("Digite um número: ")))

soma = 0
for y in range(4):
    soma = soma + numeros[y]
print("Total da soma dos números:", soma)
media = soma / 4
print("Média:", media)


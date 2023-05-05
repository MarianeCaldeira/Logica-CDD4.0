"""Escreva um algoritmo que dado um arrays, retorno um novo array, com os
elementos em ordem invertida."""

a = [1, 2, 3, 4, 5]
b = []

for x in range(4, -1, -1):
    b.append(a[x])
print(a)
print(b)


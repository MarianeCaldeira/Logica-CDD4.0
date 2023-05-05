"""Escreva um algoritmo que receba do usuário 10 números e mostre:
1. todos os números ímpares;
2. todos os números pares;
3. todos os números positivos;
4. todos os números negativos;
5. todos os zeros que aparecem no array"""

num = []
for x in range(5):
    num.append(int(input("Digite um numero: ")))
for y in range(5):
    if num[y] % 2 != 0:
        print(num[y], "é ímpar!")
for a in range(5):
    if num[a] % 2 == 0:
        print(num[a], "é par!")
for b in range(5):
    if num[b] > 0:
        print(num[b], "é positivo!")
for c in range(5):
    if num[c] < 0:
        print(num[c], "é negativo!")
for d in range(5):
    if num[d] == 0:
        print(num[d], "(zero)")

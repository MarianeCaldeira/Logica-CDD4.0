"""Crie um algaritmo que leia um número e diga se ele é par ou ímpar."""

num = float(input("Digite um número: "))

if num % 2 == 0:
    if num > 0:
        print(num, "é par e positivo")
    else:
        print(num, "é par e negativo")
else:
    if num > 0:
        print(num, "é ímpar e positivo")
    else:
        print(num, "é ímpar e negativo")

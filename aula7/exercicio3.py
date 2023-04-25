"""Ler um vetor A de 10 números. Logo em seguida, ler mais um e guardar em uma variável X.
Armazenar em um vetor M o resultado de cada elemento de A multiplicado pelo valor X.
Logo após, imprimir o vetor M."""
a = []
m = []
mult = 0
for x in range(10):
    a.append(float(input("Digite um número: ")))
num = float(input("Digite um número para a multiplicação: "))
for y in range(10):
    mult = a[y] * num
    m.append(mult)
print(a)
print(num)
print(m)

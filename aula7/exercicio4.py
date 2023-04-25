"""Faça um código para ler 5 números e amarzene em um vetor. Após a leitura total dos 5 números:
o código deve escrever esses 5 números lidos na ordem inversa."""

num = []
for x in range(5):
    num.append(float(input("Digite um número: ")))
for y in range(4, -1, -1):
    print(num[y], end=" ")

"""Outra forma de fazer:"""
"""for y in range(5):
    print(num[4-y], end=" ")"""

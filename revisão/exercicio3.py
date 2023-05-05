""" Escreva um algoritmo para ler dois valores (considere que não serão lidos valores iguais)
e escrevê-los em ordem crescente"""

n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))

if n1 == n2:
    print("Por favor, informe números diferentes!")
else:
    if n1 > n2:
        print(n2, n1)
    else:
        print(n1, n2)

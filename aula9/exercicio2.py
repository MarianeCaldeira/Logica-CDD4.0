"""Crie um algaritmo que leia um número diferente de zero e diga se este número é positivo ou negativo."""

continuar = "s"
while continuar == "s":
    n = float(input("Digite um número: "))
    if n < 0:
        print(n, "é negativo")
    elif n > 0:
        print(n, "é positivo")
    else:
        print("Digite um número diferente de zero!")
    continuar = input("Deseja informar um novo número?(s/n)")
else:
    print("PROGRAMA ENCERRADO")

resp = 1
while resp != 6:
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    while True:
        resp = int(input(
            "1. Soma\n"
            "2. Subtração\n"
            "3. Multiplicação\n"
            "4. Divisão\n"
            "5. Para digitar novo número\n"
            "6. Sair\n"
            "Selecione uma das opção a cima: "
        ))
        if resp == 1:
            print(n1, "+", n2, "=", n1 + n2)
        elif resp == 2:
            print(n1, "-", n2, "=", n1 - n2)
        elif resp == 3:
            print(n1, "*", n2, "=", n1 * n2)
        elif resp == 4:
            print(n1, "/", n2, "=", n1 / n2)
        elif resp == 5:
            break
        elif resp == 6:
            print("Programa encerrado!")
            break

"""Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10"""

num = float(input("Informe um número: "))

if num > 10:
    print(num, "É MAIOR QUE 10!")
elif num == 10:
    print("Informe um número diferente de 10!")
else:
    print(num, "NÃO É MAIOR QUE 10!")

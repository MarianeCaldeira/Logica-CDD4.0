"""Faça um algaritmo que receba duas notas e calcule a média aritmétrica"""

continuar = "s"
medias = []
while continuar == "s":
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2
    medias.append(media)
    if media >= 7:
        print("A média do aluno foi", media, "(APROVADO!)")
    elif media >= 4:
        print("A média do aluno foi", media, "(RECUPERAÇÃO!)")
    else:
        print("A média do aluno foi", media, "(REPROVADO!)")
    continuar = input("Você deseja continuar?(s/n)")
print("As médias dos alunos foram:", medias)

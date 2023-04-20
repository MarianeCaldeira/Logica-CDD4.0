"""Mostrar o nome do aluno e sua posição no array"""
alunos = []
n = int(input("Digite a quantidade de alunos na sala: "))
for x in range(n):
    nomes = input("Digite o nome do aluno: ")
    alunos.append(nomes)
for y in range(n):
    print(alunos[y], y)

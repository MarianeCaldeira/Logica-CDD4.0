"""Mostrar o nome de cada aluno, sua respectiva posição e pesquisar o nome do aluno na lista"""
alunos = []
n = int(input("Digite a quantidade de alunos na sala: "))
for x in range(n):
    nomes = input("Digite o nome do aluno: ")
    alunos.append(nomes)
for y in range(n):
    print(alunos[y], y)
nome = input("Digite o nome do aluno que deseja pesquisar: ")
cont = 0
for b in range(n):
    if alunos[b] == nome:
        print(b, alunos[b])
    else:
        cont += 1
if cont == n:
    print("Não encontrado!")

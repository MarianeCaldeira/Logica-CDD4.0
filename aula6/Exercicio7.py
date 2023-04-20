alunos = []
n = int(input("Digite a quantidade de alunos na sala: "))
for x in range(n):
    nomes = input("Digite o nome do aluno: ")
    alunos.append(nomes)
for y in alunos:
    print(y)

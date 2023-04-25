"""Escreva um código que permita a leitura das notas de uma turma de 5 alunos e guarde num vetor.
Calcule a média da turma e mostre quantos alunos obtiveram notas a cima da média da turma.
Mostre o resultado da contagem."""
nota = []
soma = 0
cont = 0
for x in range(5):
    nota.append(float(input("Digite a nota do aluno: ")))
for y in range(5):
    soma += nota[y]
media = soma / 5
print("A média da turma é", media)
for b in range(5):
    if nota[b] >= media:
        cont += 1
print(cont, "alunos conseguiram alcançar a média da turma!")

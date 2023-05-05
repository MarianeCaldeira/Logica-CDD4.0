"""Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez
(considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em
horas, sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo
pode iniciar em um dia e terminar no dia seguinte"""

inicio = int(input("Informe a hora do início do jogo: "))
fim = int(input("Informe a hora do fim do jogo: "))

if inicio < fim:
    duracao = fim - inicio
else:  # caso o jogo tenha iniciado em um dia e terminado no dia seguinte
    duracao = 24 - inicio + fim

print("A duração do jogo foi de", duracao, "horas.")

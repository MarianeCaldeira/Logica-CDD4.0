"""Escreva um algaritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos
e válidos. Calcular e escrever o porcentual que cada um representa em relação ao total de eleitores."""

total_eleitores = int(input("Informe o total de eleitores: "))
brancos = int(input("Informe o total de votos em branco: "))
nulos = int(input("Informe o total de votos nulos: "))
validos = int(input("Informe o total de votos válidos: "))

porcento_brancos = (brancos * total_eleitores) / 100
porcento_nulos = (nulos * total_eleitores) / 100
porcento_validos = (validos * total_eleitores) / 100

print("Total de eleitores:", total_eleitores)
print("Votos em brancos: ", porcento_brancos)
print("Votos nulos: ", porcento_nulos)
print("Votos válidos: ", porcento_validos)

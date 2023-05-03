"""Faça um algaritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa
expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias"""

anos = int(input("Informe quantos anos você tem: "))
meses = int(input("Informe quantos meses você tem: "))
dias = int(input("Informe quantos dias você tem: "))

ano_idade = anos * 365
meses_idade = meses * 30

dias_idade = ano_idade + meses_idade + dias
print("Seus dias de vida são", dias_idade)

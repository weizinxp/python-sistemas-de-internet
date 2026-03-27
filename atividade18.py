#18. Faça um programa que leia a quantidade de faltas de um aluno e informe se ele está dentro do limite ou acima do limite,
#considerando limite de 10 faltas.

faltas = int(input("Quantas faltas o aluno tem? "))
if faltas > 10:
    print("Está reprovado por faltas")
elif faltas == 10:
    print("Mais uma falta e é reprovado por faltas")
else:
    print("Está dentro do limite de faltas")
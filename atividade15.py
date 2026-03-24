#15. Faça um programa que leia o nome de um aluno e sua nota, informando se ele foi aprovado ou reprovado.

nome = str(input("Nome Do Aluno: "))
nota = float(input("Nota do aluno: "))
if nota >= 7:
    print(f"{nome} Está Aprovado")
else:
    print(f"{nome} Não Está Aprovado")
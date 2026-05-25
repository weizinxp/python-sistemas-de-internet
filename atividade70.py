#70. Crie uma matriz para armazenar 3 notas de 4 alunos. Depois, calcule e mostre a média de cada aluno.

matriz = []
aluno = []
notas = []
media = []
soma = 0
for i in range(4):
    aluno.append(input(f"Digite o nome do aluno: "))
    for j in range(3):
        n = float(input(f"Digite a nota do aluno: "))
        notas.append(n)
        soma += n
    media.append(soma / 3)
    soma = 0
for i in range(4):
    print(f"Aluno: {aluno[i]} - Média: {media[i]}")
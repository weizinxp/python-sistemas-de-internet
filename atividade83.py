medias = []
notas = []
alunos = []
#function to count the number of students with average >= 7
def cont_aprovados(medias):
    count = 0
    for media in medias:
        if media >= 7:
            count += 1
    return count
#for loop to get the names and grades of 4 students
for i in range(4):
    aluno = input(f"Digite o nome do aluno {i + 1}: ")
    alunos.append(aluno)
    n2 = []
    for j in range (3):
        n = float(input(f"Digite a nota {j + 1} do aluno {aluno}: "))
        n2.append(n)
    media = sum(n2) / len(n2)
    medias.append(media)
    notas.append(n2)
#apply the function to count the number of students with average >= 7
aprovados = cont_aprovados(medias)
p = input("Deseja analisar as notas? (s/n): ").strip().lower()
if p == 's':
    print(f"Quantidade de alunos aprovados: {aprovados}")
    print("Médias dos alunos:")
    for i in range(len(alunos)):
        print(f"{alunos[i]}: medias: {medias[i]:.2f} notas: {notas[i]}")
    print("Total Aprovados: ", aprovados)
else:
    print("obrigado pelo serviço boa noite.")

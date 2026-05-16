#61. 10. Sistema simples de notas
#Faça um programa que leia o nome e a nota de 5 alunos. Os nomes devem ser armazenados em uma lista e as notas em outra lista.
#Depois, o programa deve mostrar:
#Nome do aluno
#Nota
#Situação: Aprovado ou Reprovado
#Considere aprovado quem tiver nota maior ou igual a 7.
#Exemplo:
#Aluno: Maria
#Nota: 8.5
#Situação: Aprovado


NomeAluno = []
NotaAluno = []
for i in range(5):
    nome = input("Digite o nome do auno: ")
    nota = float(input("Digite a nota do aluno: "))
    NomeAluno.append(nome)
    NotaAluno.append(nota)
for i in range(len(NotaAluno)):
    if NotaAluno[i] >= 7:
        print("\n Aluno: {} \n Nota: {} \n Aprovado".format(NomeAluno[i], NotaAluno[i]))
    else:
        print("\n Aluno: {} \n Nota: {} \n Reprovado".format(NomeAluno[i], NotaAluno[i]))
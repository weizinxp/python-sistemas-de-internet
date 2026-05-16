#54. Média e valores acima da média
#Faça um programa que leia 6 notas e armazene em uma lista. Depois, calcule a média da turma e mostre quais notas ficaram acima da média.

nota = []
media = 0
maior = []
for i in range(6):
    nt = float(input("Digite a nota: "))
    nota.append(nt)
media = sum(nota) / 6

for i in range(len(nota)):
    if nota[i] >= media:
        maior.append(nota[i])
    else:
        continue
print("a media foi {:.2f} e as notas maiores que a media foram {}".format(media,maior))



nota = float(input("Digite a nota do aluno: "))
if nota >= 7:
   print("Aprovado")
elif nota >= 5:
    print("Recuperação")
elif nota > 0 or nota < 5:
    print("Reprovado")
else:
    print("Nota inválida")

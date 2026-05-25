#81. Crie uma função chamada verificar_situacao que receba uma média como parâmetro e informe se o aluno está aprovado ou reprovado, considerando aprovado quem tiver média maior ou igual a 7.

def verificar_situacao(media):
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
notas = []
for i in range(4):
    n = float(input(f"Digite a nota {i + 1}: "))
    notas.append(n)
media = sum(notas) / len(notas)
print("A média é: {:.2f}".format(media))
verificar_situacao(media)
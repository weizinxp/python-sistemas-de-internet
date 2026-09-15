#81. Crie uma função chamada verificar_situacao que receba uma média como parâmetro e informe se o aluno está aprovado ou reprovado, considerando aprovado quem tiver média maior ou igual a 7.

from atividade82 import analisar_notas


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
n = input("Deseja verificar a situação do aluno? (s/n): ").strip().lower()
if n == 's':
    verificar_situacao(media)
else:
    print("Verificação de situação não realizada.")
m = input("Deseja analisar as notas? (s/n): ").strip().lower()
if m == 's':
    analisar_notas(notas)
else:
    print("Análise de notas não realizada.")
#Crie uma função analisar_notas que receba uma lista de notas e mostre:

def analisar_notas(notas):
    if not notas:
        print("A lista de notas está vazia.")
        return
    
    media = sum(notas) / len(notas)
    maior_nota = max(notas)
    menor_nota = min(notas)
    print(f"Média das notas: {media:.2f}")
    print(f"Maior nota: {maior_nota}")
    print(f"Menor nota: {menor_nota}")

notas = []
for i in range(4):
    n = float(input(f"Digite a nota {i + 1}: "))
    notas.append(n)
p = input("Deseja analisar as notas? (s/n): ").strip().lower()
if p == 's':
    analisar_notas(notas)
else:
    print("Análise de notas não realizada.")

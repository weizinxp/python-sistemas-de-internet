#67. Crie uma matriz 3x3 e calcule a soma dos valores da diagonal principal.
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero: "))
        linha.append(n)
    matriz.append(linha)

soma = 0

for i in range(3):
    soma += matriz[i][i]

print(f"A soma da diagonal principal é: {soma}")
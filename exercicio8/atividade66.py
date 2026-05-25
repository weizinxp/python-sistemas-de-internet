#66. Crie uma matriz 3x3 e mostre apenas os valores da diagonal principal.
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero: "))
        linha.append(n)
    matriz.append(linha)
print(matriz[0][0])
print(matriz[1][1])
print(matriz[2][2])
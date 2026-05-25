#71. Crie uma matriz 3x3. Depois, mostre a soma de cada linha separadamente.

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite o valor: "))
        linha.append(n)
    matriz.append(linha)

for i in range(3):
    soma_linha = sum(matriz[i])
    print(f"Linha {i + 1}: {soma_linha}")
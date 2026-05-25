#62. Crie uma matriz 3x3 com valores digitados pelo usuário. Depois, mostre a matriz na tela em formato de tabela.

matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero:"))
        linha.append(n)
    matriz.append(linha)
print(matriz)
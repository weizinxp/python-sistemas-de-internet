#64. Crie uma matriz 3x3 com números inteiros. Depois, mostre o maior valor da matriz.

matriz = []
maior = None
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero: "))
        linha.append(n)
        if maior is None or n > maior:
            maior = n
    matriz.append(linha)
print(matriz)
print(f"O maior numero é: {maior}")
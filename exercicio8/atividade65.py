#65. Crie uma matriz 3x3 com números inteiros. Depois, mostre o menor valor da matriz.

matriz = []
menor = None
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero: "))
        linha.append(n)
        if menor is None or n < menor:
            menor = n
    matriz.append(linha)
print(matriz)
print(f"O menor numero é: {menor}")
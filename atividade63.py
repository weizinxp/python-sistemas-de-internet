#63. Crie uma matriz 2x3 com números inteiros digitados pelo usuário. Depois, mostre a soma de todos os valores da matriz.


matriz = []
soma = 0
for i in range(2):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero:"))
        linha.append(n)
        soma += n
    matriz.append(linha)
print(matriz)
print(f"A soma é: {soma}")
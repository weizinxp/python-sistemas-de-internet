#68. Crie uma matriz 3x3 e conte quantos números pares existem dentro dela.
matriz = []
par = 0
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero: "))
        linha.append(n)
        if n % 2 == 0:
            par += 1
            
    matriz.append(linha)
print(matriz)
print(f"O numero de pares é: {par}")

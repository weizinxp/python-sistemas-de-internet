#69. Crie uma matriz 3x3 e conte quantos números maiores que 10 existem dentro dela.

matriz = []
maior = 0
for i in range(3):
    linha = []
    for j in range(3):
        n = int(input(f"Digite um numero:"))
        linha.append(n)
        if n > 10:
            maior += 1
    matriz.append(linha)
print(f"a quantia de numeros maiores que 10 é: {maior}")
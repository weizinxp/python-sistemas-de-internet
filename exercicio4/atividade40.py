#40. Faça um programa que leia 10 números inteiros e mostre a soma apenas dos números positivos.

soma = 0

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º número: "))
    if valor > 0:
        soma += valor

print(soma)
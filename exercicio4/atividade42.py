# Programa para ler 8 números inteiros e informar o maior

maior = None

for i in range(8):
    numero = int(input(f"Digite o {i+1}º número: "))
    if maior is None or numero > maior:
        maior = numero

print(f"O maior número digitado foi: {maior}")
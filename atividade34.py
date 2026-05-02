#6.Faça um programa que peça 5 números ao usuário e no final mostre a soma de todos eles.

soma = 0
contador = 0

while contador < 5:
    n = int(input("Digite um número: "))
    soma += n
    contador += 1

media = soma
print("A soma é:", soma)
#35.Faça um programa que peça 5 números ao usuário e no final mostre a média deles.

soma = 0
contador = 0

while contador < 5:
    n = int(input("Digite um número: "))
    soma += n
    contador += 1

media = soma / 5
print("A média é:", media)
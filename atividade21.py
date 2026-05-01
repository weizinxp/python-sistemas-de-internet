#21. Faça um Programa que leia três números e mostre-os em ordem decrescente.Três números em ordem decrescente
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite o terceiro número: "))

numeros = [n1, n2, n3]

numeros.sort(reverse=True)

print("Números em ordem decrescente:", numeros)

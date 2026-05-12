#37. Faça um programa que leia um número inteiro e mostre todos os divisores desse número.

n = int(input('Digite Um Número: '))

for i in range(1, n + 1):
    if n % i == 0:
    print(i)
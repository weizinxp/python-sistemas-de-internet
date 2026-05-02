#3.Faça um programa que peça ao usuário um número e depois mostre a tabuada desse número de 1 até 10 usando while.

n = 0
n2 = int(input('Digite um número: '))
while n <= 9:
    n += 1
    print("{} x {} = {}".format(n2, n, n * n2))
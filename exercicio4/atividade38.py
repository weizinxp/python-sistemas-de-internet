#38. Faça um programa que leia um número inteiro e informe quantos divisores ele possui.

n = int(input('Digite Um Número: '))

contador = 0

for i in range(1, n + 1):
    if n % i == 0:
        contador += 1
print('o numero tem {} divisores'.format(contador))
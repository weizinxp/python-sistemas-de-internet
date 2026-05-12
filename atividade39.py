#39. Faça um programa que leia um número inteiro e informe se ele é primo ou não.

n = int(input('Digite um número: '))

contador = 0

for i in range(1, n + 1):
    if n % i == 0:
        contador += 1

if contador == 2:
    print('É primo')
else:
    print('Não é primo')
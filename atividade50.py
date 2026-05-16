#50. Crie um programa que leia 5 números e mostre apenas os números maiores que 10.

num = []
for i in range(5):
    n = int(input('Digite um numero: '))
    if n >= 10:
        num.append(n)
print('Os numeros maiores ou iguais a 10 são: {}'.format(num))

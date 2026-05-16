#51. Crie um programa que leia 5 números e mostre a soma dos números digitados.

num = []
for i in range(5):
    n = int(input('Digite um numero: '))
    soma = sum(num)
    num.append(n)
print('A soma dos numeros {} é: {}'.format(num, soma))
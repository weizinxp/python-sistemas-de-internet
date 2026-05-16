#48. Crie um programa que leia 5 idades e mostre quantas pessoas são maiores de idade.

idade = []
n = 0
for i in range(5):
    id = int(input('Digite sua idade: '))
    idade.append(id)
    if id >= 18:
        n += 1
print('O numero de pessoas maiores de idade é: {}'.format(n))


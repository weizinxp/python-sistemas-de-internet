#47. Crie um programa que leia 7 números e mostre o menor número digitado.

n = []
for i in range(7):
    num = int (input('Digite um numero: '))
    n.append(num)
    menor_num = min(n)
print('O menor numero é: {}'.format(menor_num))


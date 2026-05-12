n = []
for i in range(7):
    num = int (input('Digite um numero: '))
    n.append(num)
    menor_num = min(n)
print('O menor numero é: {}'.format(menor_num))

#2.
idade = []
n = 0
for i in range(5):
    id = int(input('Digite sua idade: '))
    idade.append(id)
    if id >= 18:
        n += 1
print('O numero de pessoas maiores de idade é: {}'.format(n))

#3.

produto = []
for i in range(4):
    valor =float(input('Digite o valor do produto: '))
    produto.append(valor)
    total = sum(produto)
print('O valor total da compra é: R${:.2f}'.format(total))

#4.
num = []
for i in range(5):
    n = int(input('Digite um numero: '))
    if n >= 10:
        num.append(n)
print('Os numeros maiores ou iguais a 10 são: {}'.format(num))

#5.
num = []
for i in range(5)
    n = int(input('Digite um numero: '))
    soma = sum(num)
    num.append(n)
print('A soma dos numeros {} é: {}'.format(num, soma))
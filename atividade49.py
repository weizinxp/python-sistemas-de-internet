#49. Crie um programa que leia 4 preços de produtos e mostre o valor total da compra.

produto = []
for i in range(4):
    valor =float(input('Digite o valor do produto: '))
    produto.append(valor)
    total = sum(produto)
print('O valor total da compra é: R${:.2f}'.format(total))


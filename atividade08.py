#8. Faça um programa que peça o valor de um produto e o percentual de desconto, calculando quanto o produto passará a custar após o desconto.

produto = float(input('Digite o valor do produto: '))
percentual_desconto = float(input('Quanto é o desconto do produto? '))
desconto = produto - (produto * percentual_desconto / 100)
print('O valor do produto com desconto de {}% é: {}'.format(percentual_desconto,desconto))
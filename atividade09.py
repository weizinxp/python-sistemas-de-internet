#9. Elabore um programa que peça ao usuário uma temperatura em graus Celsius e mostre o valor correspondente em Fahrenheit.

celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celsius * 1.8) + 32
print('A temperatura em Fahrenheit é: {}'.format(fahrenheit))
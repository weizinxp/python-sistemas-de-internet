#7. Crie um programa que peça a base e a altura de um triângulo, calcule sua área e mostre o resultado na tela.

base = float(input('Digite a base do triangulo: '))
altura = float(input('Digite a altura do triangulo: '))
area = (base * altura) / 2
print('A área do triângulo é: {}'.format(area))
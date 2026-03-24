#11. Faça um programa que leia a idade de uma pessoa e informe se ela pode votar, considerando idade mínima de 16 anos.

idade = int(input("Diga a sua idade: "))
if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não pode votar")
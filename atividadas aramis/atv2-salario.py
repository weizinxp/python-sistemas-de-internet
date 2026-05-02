#Faça um programa que leia o salário de uma pessoa e informe se ela recebe
#acima de 2000 reais ou 2000 reais ou menos.

salario = int(input("Digite o seu salário:" ))
if salario >= 2000:
    print("você recebe acima de 2000")
elif salario == 2000:
    print("você recebe exatamente 2000")
else:
    print("você recebe abaixo de 2000")
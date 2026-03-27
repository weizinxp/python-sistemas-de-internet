#13. Faça um programa que leia o salário de uma pessoa e informe se ela recebe acima de 2000 reais ou 2000 reais ou menos.

salario = int(input("Digite o valor do seu salário: "))
if salario > 2000:
    print("Recebe acima de 2000 reais")
else:
    print("Recebe 2000 reais ou menos")
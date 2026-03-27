#17. Faça um programa que leia um número e informe se ele é maior que 10 ou menor ou igual a 10.

print("Diga um número pra conferir se é maior que 10")
numero = int(input("Número: "))
if numero > 10:
    print("O número é maior que 10")
elif numero == 10:
    print("O número é 10")
else:
    print("O número não é maior que 10")
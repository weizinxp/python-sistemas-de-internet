#1. Faça um programa que leia a idade de uma pessoa e informe se ela pode votar,
#considerando que a idade mínima para votar é 16 anos.

print("diga sua idade pra saber seu direito a voto")
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Você tem direito a votar")
else:
    print("Você não tem direito a votar")
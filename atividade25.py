#25. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor
#deve aparecer valor inválido.

dia = int(input("Digite o dia: "))
dias = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira",
        "Quinta-feira", "Sexta-feira", "Sábado"]

if 1 <= dia <= 7:
    print(dias[dia - 1])
else:
    print("Dia inválido")
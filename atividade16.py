#16. Faça um programa que leia a idade de uma pessoa e informe se ela pode entrar no evento,
#considerando entrada permitida apenas para maiores de 18 anos.

print("Diga sua idade para conferir se pode entrar no evento")
idade = int(input("Idade: "))
if idade >= 18:
    print("Você pode entrar no evento")
else:
    print("Você não pode entrar no evento")
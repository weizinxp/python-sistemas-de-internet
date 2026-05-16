#56. Verificar se existem números repetidos
#Faça um programa que leia 8 números e armazene em uma lista. Depois, informe se existem números repetidos na lista.
#Exemplo:
#Existem números repetidos.
#ou
#Não existem números repetidos.


repetido = []
num = []
for i in range(10):
    n = int(input("Digite um numero: "))
    if n in num:
        repetido.append(n)
    else:
        num.append(n)
print("Os numeros repetidos são: {}".format(repetido))

#55. Contagem de números positivos, negativos e zeros
#Faça um programa que leia 10 números e armazene em uma lista. Depois, mostre:
#Quantidade de positivos
#Quantidade de negativos
#Quantidade de zeros

positivo = []
negativo = []
zero = []
for i in range(10):
    n = int(input("Digite um numero: "))
    if n > 0:
        positivo.append(n)
    elif n < 0:
        negativo.append(n)
    else:
        zero.append(n)
print("a quantia de numeros positivos é {}, a quantia de numeros negativos é {} e a quantia de zeros é {}".format(len(positivo), len(negativo), len(zero)))

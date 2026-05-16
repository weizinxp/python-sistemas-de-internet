#53. Separar pares e ímpares
#Faça um programa que leia 10 números e armazene em uma lista. Depois, crie duas novas listas: uma contendo os números pares e outra contendo os números ímpares.
#No final, mostre as três listas:
#Lista original: [...]
#Pares: [...]
#Ímpares: [...]


lista1 = []
par = []
impar = []

for i in range(10):
    n = (int(input("Digite um número: ")))
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    lista1.append(n)
print("Números pares: {}".format(par))
print("Números ímpares: {}".format(impar))
print("Lista completa: {}".format(lista1))
#58. Soma dos números pares e soma dos números ímpares
#Faça um programa que leia 10 números e armazene em uma lista. Depois, calcule separadamente:
#Soma dos pares
#Soma dos ímpares

lista1 = []
par = []
impar = []
parsoma = 0
imparsoma = 0

for i in range(10):
    n = (int(input("Digite um número: ")))
    if n % 2 == 0:
        parsoma += n
        par.append(n)
    else:
        impar.append(n)
        imparsoma += n
    lista1.append(n)

print("Lista original:", lista1)
print("Números pares:", par)
print("Soma dos números pares:", parsoma)
print("Números ímpares:", impar)
print("Soma dos números ímpares:", imparsoma)
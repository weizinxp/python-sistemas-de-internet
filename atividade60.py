#60. 9. Criar uma lista apenas com números maiores que 10
#Faça um programa que leia 8 números e armazene em uma lista. Depois, crie uma nova lista contendo apenas os números maiores que 10.
#No final, mostre:
#Lista original: [...]
#Números maiores que 10: [...]

listaA = []
listaB = []
for i in range(8):
    n = int(input("Digite um número: "))
    listaA.append(n)
for i in range(len(listaA)):
    if listaA[i] >= 10:
        listaB.append(listaA[i])
print("Lista A:", listaA)
print("Lista B:", listaB)
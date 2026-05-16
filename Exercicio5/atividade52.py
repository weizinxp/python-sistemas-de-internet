#52. Maior número e sua posição
#Faça um programa que leia 8 números e armazene em uma lista. Depois, mostre o maior número digitado e a posição em que ele aparece na lista.
#Exemplo de saída:
#Maior número: 25
#Posição: 3


numero = []
for i in range(8):
    numero.append(int(input("Digite um número: ")))
    maior = max(numero)
posicao = numero.index(maior)
print("O maior é {} e está na posição {}".format(maior, posicao))
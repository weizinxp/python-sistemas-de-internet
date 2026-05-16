#6. Inverter a lista sem usar reverse
#Faça um programa que leia 7 números e armazene em uma lista. Depois, crie uma nova lista com os valores na ordem inversa.
#Atenção: não use reverse().
#Exemplo:
#Lista original: [1, 2, 3, 4, 5, 6, 7]
#Lista invertida: [7, 6, 5, 4, 3, 2, 1]


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listainvertida = []
for i in range(9, -1, -1):
    listainvertida.append(lista[i])
print(listainvertida)
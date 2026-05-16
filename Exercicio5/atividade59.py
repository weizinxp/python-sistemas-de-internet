#8. Buscar número e mostrar quantas vezes aparece
#Faça um programa que leia 10 números e armazene em uma lista. Depois, peça ao usuário um número para pesquisar.
#O programa deve informar quantas vezes esse número aparece na lista.
#Exemplo:
#Digite um número para buscar: 5
#O número 5 aparece 3 vezes.


lista = []
for i in range(10):
    n = int(input("Digite um numero: "))
    lista.append(n)
busca = int(input("Digite um numero para buscar: "))
quantia = lista.count(busca)
if quantia > 0:
    print("O numero {} aparece {} vezes na lista".format(busca, quantia))
else:
    print("O numero {} não aparece na lista".format(busca))
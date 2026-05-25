#80. Crie uma função chamada calcular_media que receba duas notas como parâmetro e mostre a média entre elas.

def calcular_media(notas):
    media = sum(notas) / len(notas)
    print("A média é: {:.2f}".format(media))
notas = []
for i in range(2):
    n = float(input(f"Digite a nota {i + 1}: "))
    notas.append(n)
calcular_media(notas)

#45. Programa para exibir a tabuada de um número inteiro de 1 a 20, mostrando apenas os resultados pares

numero = int(input("Digite um número inteiro: "))

for i in range(1, 21):
    resultado = numero * i
    if resultado % 2 == 0:
        print(f"{numero} x {i} = {resultado}")
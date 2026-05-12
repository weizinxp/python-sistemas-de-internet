#43.py Programa para ler 8 números inteiros e informar o menor

numeros = []
for i in range(8):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

menor = min(numeros)
print(f"O menor número digitado foi: {menor}")
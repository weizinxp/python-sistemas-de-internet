#75. Crie uma função chamada somar que receba dois números como parâmetro e mostre a soma entre eles.

def somar (n1, n2):
    soma = n1 + n2
    print(f"A soma é: {soma}")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
somar(n1, n2)
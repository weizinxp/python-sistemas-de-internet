#76. Crie uma função chamada subtrair que receba dois números como parâmetro e mostre a subtração entre eles.

def subtrair (n1, n2):
    subtracao = n1 - n2
    print(f"A subtração é: {subtracao}")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
subtrair(n1, n2)
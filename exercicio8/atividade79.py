#79. Crie uma função chamada verificar_positivo que receba um número como parâmetro e mostre se ele é positivo, negativo ou zero.
def verificar_positivo(numero):
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
n = int(input("Digite um número: "))
verificar_positivo(n)
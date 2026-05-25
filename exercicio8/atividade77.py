#77. Crie uma função chamada mostrar_dobro que receba um número como parâmetro e mostre o dobro desse número.

def mostrar_dobro(numero):
    dobro = numero * 2
    print(f"O dobro de {numero} é: {dobro}")
n = int(input("Digite um número: "))
mostrar_dobro(n)
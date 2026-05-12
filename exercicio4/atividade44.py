#44. Faça um programa que leia um número inteiro e mostre o fatorial desse número.

def fatorial(n):
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def main():
    try:
        n = int(input("Digite um número inteiro: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if n < 0:
        print("Fatorial não definido para números negativos.")
    else:
        print(f"O fatorial de {n} é {fatorial(n)}")

if __name__ == "__main__":
    main()
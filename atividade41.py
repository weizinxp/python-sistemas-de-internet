#41. Faça um programa que leia 10 números inteiros e mostre quantos são pares e quantos são ímpares.

def main():
    pares = 0
    impares = 0

    for i in range(10):
        valor = int(input(f"Digite o {i + 1}º número inteiro: "))
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"Pares: {pares}")
    print(f"Ímpares: {impares}")


if __name__ == "__main__":
    main()
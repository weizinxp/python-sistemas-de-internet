#46. Faça um programa que leia 10 números inteiros e mostre a média apenas dos números maiores que zero.

def main():
    soma = 0
    contador = 0

    for i in range(10):
        try:
            num = int(input(f"Digite o {i + 1}º número inteiro: "))
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
            return

        if num > 0:
            soma += num
            contador += 1

    if contador > 0:
        media = soma / contador
        print(f"Média dos números maiores que zero: {media:.2f}")
    else:
        print("Não foi possível calcular a média porque nenhum número positivo foi digitado.")


if __name__ == "__main__":
    main()
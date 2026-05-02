#33.Faça um programa que peça ao usuário um número maior que zero. Caso ele digite um valor inválido,
#o programa deve continuar pedindo até que ele digite um número válido.

n = input('Digite um número maior que zero: ')

while n.isdigit():
    print(n)
    n = input('Digite um número maior que zero: ')

print("Entrada inválida, encerrando.")
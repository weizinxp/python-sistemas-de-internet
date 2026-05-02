soma = 0

while True:
    n = int(input("Digite um número: "))
    soma += n
    if n == 0:
        break
    else: 
        continue
print("A soma é:", soma)
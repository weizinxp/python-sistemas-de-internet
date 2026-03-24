#4. Crie um programa que peça ao usuário a quantidade de quilômetros percorridos e a quantidade de litros de combustível gastos,
#e depois mostre o consumo médio do veículo.

km = float(input('quanto km pecorridos? '))
litros = float(input('quantos litros usado? '))
result = km / litros
print("o consumo medio foi de {}".format(result))
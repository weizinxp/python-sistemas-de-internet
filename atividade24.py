#24. Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do
#salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário
#o valor da sua hora e a quantidade de horas trabalhadas no mês


horas = float(input("Digite o número de horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora trabalhada: "))

salario = horas * valor_hora
if salario <= 900:
    desconto = 0
    percentual = 0

elif salario <= 1500:
    desconto = salario * 0.05
    percentual = 5
elif salario <= 2500:
    desconto = salario * 0.10
    percentual = 10
elif salario > 2500:
    desconto = salario * 0.20
    percentual = 20
else:
    print("Digite um salário válido")
desconto_inss = salario * 0.10
salario_liquido = salario - desconto - desconto_inss
fgts = salario * 0.11
total_descontos = desconto + desconto_inss

print(f"Salário Bruto: R$ {salario:.2f}")
print(f"(-) IR ({percentual}%): R$ {desconto:.2f}")
print(f"(-) INSS (10%): R$ {desconto_inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
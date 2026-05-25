#78. Crie uma função chamada verificar_idade que receba a idade de uma pessoa como parâmetro e mostre se ela é maior ou menor de idade.
def verificar_idade(idade):
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
idade_usuario = int(input("Digite sua idade: "))
verificar_idade(idade_usuario)
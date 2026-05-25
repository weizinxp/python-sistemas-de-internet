#74. Crie uma função chamada mostrar_nome que receba um nome como parâmetro e mostre o nome informado pelo usuário.

def mostrar_nome(nome):
    print(f"Olá, {nome}!")
nome_usuario = input("Digite seu nome: ")
mostrar_nome(nome_usuario)
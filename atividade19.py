#19. Faça um programa que leia uma senha e informe se ela está correta ou incorreta, considerando a senha python123.

senha_correta = "python123"
senha = input("Digite a senha: ")
if senha == senha_correta:
    print("Senha correta")
else:
    print("Senha incorreta")

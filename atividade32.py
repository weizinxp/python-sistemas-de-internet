#32.Faça um programa que peça ao usuário para digitar uma senha. O programa só deve parar quando ele digitar a senha correta: 1234.

senha = "1234"
while True:
    senha_usuario = (input('Digite a senha: '))
    if senha_usuario == senha:
        print('Acesso Permitido')
        break
    else:
        print('Senha Incorreta, tente novamente.')
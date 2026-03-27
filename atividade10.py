#10. Crie um programa que peça o nome do aluno e três notas, calcule a média final e mostre uma mensagem com o nome do aluno e sua média.

nome = str(input('Diga o nome do aluno: '))
nt1 = float(input('diga a primeira nota: '.format(nome)))
nt2 = float(input('Diga a segunda nota: '))
nt3 = float(input('Diga a terceira nota: '))
media = (nt1 + nt2 + nt3) / 3
print('A média do aluno {} é: {:.2f}'.format(nome, media))
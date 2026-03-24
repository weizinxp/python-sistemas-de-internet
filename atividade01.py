#1. Crie um programa que peça o nome de uma pessoa, o curso em que ela estuda e o período atual,
#e depois mostre todas essas informações em uma frase organizada.

nome = str(input('Diga seu nome: '))
curso = str(input('Diga seu curso: '))
periodo = str(input('diga seu periodo: '))
print('Olá {} você faz {} e você ta no {} periodo'.format(nome, curso, periodo))
notas = []
for i in range(10):
    nota = float(input('Digite uma nota: '))
    notas.append(nota)
    media = sum(notas) / len(notas)
print('A media de notas é :{:.2f} '.format(media))
r = input('Deseja Ver todas as notas? (s/n) ').capitalize()
if r == 'S':
    print('As notas são: '.format(notas))
    for i in range(len(notas)):
        print('Nota {}: {:.2f}'.format(i + 1, notas[i]))
    print('---Obrigado por usar o programa!---')
else:
    print('---Obrigado por usar o programa!---')
aluno = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    aluno.append([nome, [n1, n2], media])

    op = str(input('Quer continuar S/N? '))
    if op in 'Nn':
        break

print('No. NOME         MÉDIA')
for i in range(len(aluno)):
    print(f'{i:<4}', end='')
    print(f'{aluno[i][0]:<11}', end='')
    print(f'{aluno[i][2]:>5}', end='')
    print()

while True:
    a = int(input('Mostrar nota de qual aluno? '))
    print(f'Notas de {aluno[a][0]} são: {aluno[a][1]}')

    op = str(input('Quer continuar S/N? '))
    if op in 'Nn':
        break
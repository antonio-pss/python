pessoa = dict()
galera = list()

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        else:
            print('Escreva apenas M ou F.')
    pessoa['Idade'] = int(input('Idade: '))

    galera.append(pessoa.copy())

    op = str(input('Quer continuar S/N? '))
    if op in 'Nn':
        break

print(galera)
print(len(galera))
media = 0
print('Mulheres: ')
for i in range(len(galera)):
    media += galera[i]['Idade']

    if galera[i]['Sexo'] == 'F':
        print(galera[i], end=' ')



media /= len(galera)
print(media)

print('Idadade maior que a media.')
for i in range(len(galera)):
    if galera[i]['Idade'] > media:
        print(galera[i])
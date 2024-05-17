lista = []
while True:
    j = int(input(f'Valor: '))
    if j not in lista:
        lista.append(j)
    r = str(input('Quer continuar S/N? '))
    if r in 'Nn':
        break
print(sorted(lista))
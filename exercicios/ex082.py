lista = []
pares = []
impares = []
for i in range(10):
    lista.append(int(input(f'Valor {i}: ')))
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f'Lista: {lista}')
print(f'Pares: {pares}')
print(f'Impares: {impares}')

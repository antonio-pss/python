matriz = [[], [], []]
pares = 0
coluna3 = 0
for i in range(3):
    for j in range(3):
        matriz[i].append(int(input('Valor: ')))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]
        if j == 2:
            coluna3 += matriz[i][j]

print(matriz[0])
print(matriz[1])
print(matriz[2])

print(f'Soma dos números pares: {pares}')
print(f'Soma dos valores na coluna 3: {coluna3}')
print(f'Maior valor da segunda linha: {max(matriz[1])}')
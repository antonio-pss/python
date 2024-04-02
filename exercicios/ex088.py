from random import randint
jogos = int(input('Quantos jogos serão: '))
matriz = []
aleatorios = []

for i in range(jogos):
    for j in range(6):
        aleatorios.append(randint(1, 60))
    matriz.append(aleatorios[:])
    aleatorios.clear()

for i in range(jogos):
    print(matriz[i])


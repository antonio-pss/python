lista = []
for i in range(5):
    j = input(f'Valor {i}: ')
    if i == 0 or j > max(lista):
        lista.append(j)
    elif j < min(lista):
        lista.insert(0, j)
    else:
        for i, c in enumerate(lista):
            if j >= c:
                lista.insert(i+1, j)
                break


print(lista)
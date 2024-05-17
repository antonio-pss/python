lista = []
for i in range(5):
    lista.append(input(f'Valor {i}: '))


print(f'O maior valor da lista é {max(lista)}, nas posições: ', end=' ')
for i in range(5):
    if lista[i] == max(lista):
        print(f'{i}...', end='')
print()

print(f'O maior valor da lista é {min(lista)}, nas posições: ', end=' ')
for i in range(5):
    if lista[i] == min(lista):
        print(f'{i}...', end='')
print()
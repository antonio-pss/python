lista = []
for i in range(5):
    lista.append(int(input(f'Valor {i}: ')))

print(f'Números digitados: {len(lista)}')
listaR = lista[:]
listaR.sort(reverse=True)
print(f'Em ordem decrescente: {listaR}')
if 5 in lista:
    print(f'Valor 5 foi digitado na posição: {lista.index(5)}')
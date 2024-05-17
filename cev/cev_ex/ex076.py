tupla = ('a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5)

print('-'*30)
print('LISTAGEM DE PREÇOS')
print('-'*30)

i = 0
while (i < len(tupla)):
    print(f'{tupla[i]:.<20}R$ {tupla[i+1]:>6}')
    i+=2
tupla = ('qwer', 'tyui', 'asdf', 'ghjk', 'zxcv', 'plokm')

for i in tupla:
    print(f'Na palavra {i} temos ', end=' ')
    for l in i:
        if l in 'AEIOUaeiou':
            print(f'{l}', end=' ')
    print()
num = (int(input('1: ')), int(input('2: ')), int(input('3: ')), int(input('4: ')), int(input('5: ')),)
print(f'Foi digitado {num.count(9)} números 9.')
print(f'Foi encontrado o número 3 pela primeira vez na posição {num.index(3)}')
print('Números pares: ', end=' ')
for i in num:
    if i % 2 == 0:
        print(f'{i} ', end=' ')
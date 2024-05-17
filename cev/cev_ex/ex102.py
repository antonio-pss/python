def fatorial(num, show=False):
    fat = 1
    i = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{i}', end=' ')
        if i == 1:
            print('=', end=' ')
        fat *= i
    return fat


print(fatorial(5, True))
print(fatorial(10))
def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if f < i or p < 0:
        while i >= f:
            print(i, end=' ')
            i -= p
    else:
        while i <= f:
            print(i, end=' ')
            i += p
    print('FIM!')

# PP
contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))

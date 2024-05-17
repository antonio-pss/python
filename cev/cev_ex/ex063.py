n = int(input('Escreva quantos elementos de fibonacci você quer ver: '))

a = 0
b = 0
c = 0

for i in range(n):
    if i == 0:
        print(a, end=' ')
    elif i == 1:
        a = 1
        print(a, end=' ')
    else:
        c = b
        b = a
        a = b + c
        print(a, end=' ')

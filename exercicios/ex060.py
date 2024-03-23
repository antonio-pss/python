num = int(input('Escreva um número: '))
fatorial = 1

while num > 0:
    fatorial *= num
    if num != 1:
        print(f'{num} *', end=' ')
    else:
        print(f'{num} =', end=' ')
    num -= 1
print(fatorial)

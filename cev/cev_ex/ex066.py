n = s = cont = 0
print('Escreva "999" para sair.')
while True:
    n = float(input(f'Escreva o número {cont+1}: '))
    cont+=1
    if n == 999:
        break
    s += n
print(f'A soma dos números foi {s}')
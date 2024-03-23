soma = 0

for i in range(0 ,5):
    num = int(input('Escreva um número: '))
    if num % 2 == 0:
        soma += num

print(f'A soma dos números pares é {soma}.')
numeros = [[], []]
num = 0
while True:
    num = int(input('Escreva um número inteiro: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

    op = str(input('Quer continuar S/N? '))
    if op in 'Nn':
        break

numeros[0].sort()
numeros[1].sort()
print(numeros)
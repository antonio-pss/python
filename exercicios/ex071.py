valor = int(input('Escreva o valor que quer sacar (inteiro): '))
c50 = 0
c20 = 0
c10 = 0
c1 = 0

while True:
    if valor - 50 >= 0:
        valor -= 50
        c50 += 1
    elif valor - 20 >= 0:
        valor -= 20
        c20 += 1
    elif valor - 10 >= 0:
        valor -= 10
        c10 += 1
    elif valor - 1 >= 0:
        valor -= 1
        c1 += 1


    if valor == 0:
        break

print(f'Foram sacadas {c50} notas de 50, {c20} notas de 20, {c10} notas de 10 e {c1} notas de 1.')
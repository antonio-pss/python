valor = int(input('Que valor você quer sacar? R$'))
ced = 50
cedulas = 0

while True:
    if valor >= ced:
        valor -= ced
        cedulas +=1
    else:
        print(f'O total de cédulas de {ced} foi {cedulas}')
        if ced == 50:
            ced = 20
            cedulas = 0
        elif ced == 20:
            ced = 10
            cedulas = 0
        elif ced == 10:
            ced = 1
            cedulas = 0
        else:
            break
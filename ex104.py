def leiaInt():
    var = 0
    while True:
        var = input('Valor: ')
        if var.isnumeric():
            return var
        else:
            print('ERRO')

v = leiaInt()
print(f'Valor digitado foi {v}')
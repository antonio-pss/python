n1 = float(input('Escreva um primeiro valor: '))
n2 = float(input('Escreva um segundo valor: '))
sair = False

while not sair:
    print('\n[1] Soma.')
    print('[2] Multiplicar.')
    print('[3] Maior.')
    print('[4] Novos números.')
    print('[5] Sair')
    escolha = int(input('Sua escolha: '))

    if escolha == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    elif escolha == 2:
        print(f'{n1} * {n2} = {n1*n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior entre os dois é {n1}.')
        else:
            print(f'O maior entre os dois é {n2}')
    elif escolha == 4:
        n1 = int(input('Escreva um primeiro valor: '))
        n2 = int(input('Escreva um segundo valor: '))
    elif escolha == 5:
        sair = True
    else:
        print('Você digitou errado.')
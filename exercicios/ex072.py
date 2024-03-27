tupla = ('Um', 'Dois', 'Três', 'Quatro', 'Cinco')

print('Escreva qualquer número não pedido para sair.')
while True:
    escolha = int(input('Escreva um número de 1 a 5: '))
    if 1 <= escolha <= 5:
        print(f'O número digitado por extenso é: {tupla[escolha - 1]}')
    else:
        print('Número não aceito.')
        break
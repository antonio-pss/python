print('Escreva um número negativa para sair.')

while True:
    tabuada = int(input('Escreva um número para mostrar sua tabuada: '))
    if tabuada < 0:
        break
    for i in range(11):
        print(f'{tabuada} * {i} = {tabuada*i}')
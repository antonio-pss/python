# Declaração de Variáveis e Entrada de Dados
num = int(input("Digite um número: "))
total = 1

# Lógica do Programa e Saída de Dados
if num > -1:
    print('0', end=' ')
    for i in range(num+1):
        j = 1
        for j in range(i):
            print(f'{i} ', end=' ')
            total+=1
        print('')
    print(f'\nO total de números que aparecem na sequência é {total}.')
else:
    print('\nA sequência não aceita números negativos.')
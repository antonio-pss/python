# Declaração de Variáveis e Entrada de Dados
dividendo = int(input('Digite o dividendo da divisão: '))
divisor = int(input('Digite divisor da divisão: '))

# Processamento e Saída de Dados
if divisor == 0: # Exceção
    print('A divisão é impossível.')
else:
    print(f'O quociente da divisão é: {dividendo // divisor}')
    print(f'O resto da divisão é: {dividendo % divisor}')
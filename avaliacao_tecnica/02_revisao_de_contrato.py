# Declaração de Variáveis e Entrada de Dados.
numero_falho = int(input('Digite o número falho: '))
valor_sem_falha = int(input('Digite o valor total sem falha: '))

# Variável que recebe o interio como uma lista de strings.
digitos = list(str(valor_sem_falha))

# Lógica do Programa
for i in range(len(digitos)):
    if digitos[i] == str(numero_falho):
        digitos[i] = ''

# Variável que recebe a lista de string corrigida.
valor_correto = int(''.join(digitos))

# Saída de Dados.
print(valor_correto)
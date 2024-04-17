# Declaração de Variáveis e Entrada de Dados
texto = str(input('Digite o texto que será descriptografado: '))
metade = len(texto) // 2
nova_string = ''

# Lógica para mudar a letra para uma nova na tabela ASCII.
for i, char in enumerate(texto):
    if i < metade:
        nova_string += char
    else:
        nova_string += chr(ord(char) + 1)
print(nova_string)

# Função para inverter a string.
nova_string = nova_string[::-1]
print(nova_string)

texto = '' # Limpar a variável texto para receber a última descriptografia.

# Lógica para mudar a letra para uma nova na tabela ASCII.
for i, char in enumerate(nova_string):
    if chr(ord(char) - 3) > 'A' and chr(ord(char) - 3) < '}': # Condição para limitar a descriptografia.
        texto += chr(ord(char) - 3)
    else:
        texto += char

# Saída de Dados.
print(texto)

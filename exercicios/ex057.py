sexo = ''

# while(sexo != 'M' or sexo != 'F'):
#     sexo = input('Escreva o sexo (M para Masculino e F para Feminino): ')

while sexo not in 'MF':
    sexo = input('Escreva o sexo (M para Masculino e F para Feminino): ').upper()
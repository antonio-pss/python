num = 0
soma = -999
print('Escreva 999 para sair do loop.')

while num != 999:
    num = int(input('Escreva um número: '))
    soma += num

print(f'A soma de todos os números é: {soma}')
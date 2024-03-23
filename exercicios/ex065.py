"""
sair = False
media = 0
contador = 0

num = int(input('Escreva um número: '))
media += num
contador += 1

maior = num
menor = num

desejo = input('Você deseja continuar S/N? ')
if desejo == 'N':
    sair = True

while not sair:
    num = int(input('Escreva um número: '))
    media += num
    contador += 1

    if num > maior:
        maior = num
    if num < menor:
        menor = num

    desejo = input('Você deseja continuar S/N? ')
    if desejo == 'N':
        sair = True

print(f'\nA média de todos os números digitados é {media}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
"""
soma = cont = 0
print('Escreva 999 para sair.')
while True:
    num = int(input('Escreva um número: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'A soma dos valores é {soma}')
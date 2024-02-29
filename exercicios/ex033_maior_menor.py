cont = int(input('Digite quantos valores você quer digitar: '))
ap = 1
maior = -9999999999999999
menor = 999999999999999
while cont > 0:
    valor = int(input(f'Digite o valor do {ap}° número: '))
    cont -= 1
    ap += 1
    if maior < valor:
        maior = valor
    if menor > valor:
        menor = valor

print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')
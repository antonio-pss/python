maior = 0
menor = 0

for p in range(3):
    peso = float(f'Escreva o peso da {p+1}º pessoa: ')
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso foi {maior}.')
print(f'O menor peso foi {menor}.')
from datetime import date

maior = 0
menor = 0


for i in range(3):
    ano = int(input(f'Escreva o ano que nasceu a {i+1}º pessoa: '))
    idade = date.today().year - ano
    if idade < 18:
        menor += 1
    else:
        maior += 1

print(f'{maior} pessoas são maiores de idade.')
print(f'{menor} pessoas são menores de idade.')
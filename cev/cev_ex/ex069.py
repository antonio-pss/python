mais18 = 0
homens = 0
mulher20 = 0

while True:
    sexo = 'S'
    escolha = 'E'
    idade = int(input('Escreva a idade: '))
    while sexo not in 'MFmf':
        sexo = str(input('Escreva o sexo (M/F): '))

    if sexo in 'Mm':
        homens+=1
    else:
        if idade < 20:
            mulher20+=1

    if idade > 18:
        mais18+=1

    while escolha not in 'SsNn':
        escolha = str(input('Você quer continuar (S/N)? '))

    if escolha in 'Nn':
            break

print(f'\nPessoas com mais de 18 anos: {mais18}')
print(f'Homens cadastrados: {homens}')
print(f'Mulheres com menos de 20 anos: {mulher20}')





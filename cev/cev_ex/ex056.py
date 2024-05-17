media = 0
i = 0
homem_velho = 0
mulher_menos20 = 0

for i in range(3):
    nome = str(input(f'Escreva o nome da {i+1} pessoa: '))
    idade = int(input(f'Escreva a idade da {i+1} pessoa: '))
    sexo = str(input(f'Escreva o sexo da {i+1} pessoa ("Masculino" ou "Feminino"): '))
    media += idade
    if sexo == 'Masculino':
        if idade > homem_velho:
            homem_velho = idade
    elif sexo == 'Feminino':
        if idade < 20:
            mulher_menos20 += 1
    else:
        print('Você não digito o sexo corretamente.')
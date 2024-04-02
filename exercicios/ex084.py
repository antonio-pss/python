pessoas = []
dados = list()
pesado = 0
leve = 0
while True:
    dados.append(str(input(f'Nome: ')))
    dados.append(float(input(f'Peso: ')))
    pessoas.append(dados[:])

    if len(pessoas) == 0:
        pesado = leve = dados[1]

    if dados[1] < leve:
        leve = dados[1]
    if dados[1] > pesado:
        pesado = dados[1]

    dados.clear()

    op = str(input('Quer continuar S/N? '))
    if op in 'Nn':
        break

print(f'Pessoas cadastradas: {len(pessoas)}')
print(f'Mais leve: {leve}')
print(f'Mais pesado: {pesado}')
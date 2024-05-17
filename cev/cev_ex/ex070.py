total = 0
prod_mil = 0
nome_barato = ''
menor = 1000000000000

while True:
    escolha = 'E'
    nome = str(input('Escreva o nome do produto: '))
    preco = float(input('Escreva o preço do produto: R$'))

    total += preco

    if preco > 100:
        prod_mil += 1

    if preco < menor:
        nome_barato = nome



    while escolha not in 'SsNn':
        escolha = str(input('Você quer continuar (S/N)? '))
    if escolha in 'Nn':
            break

print(f'Total da compra: R${total}')
print(f'Número de produtos que custam mais de R$1000: {prod_mil}')
print(f'Nome do produto mais barato: {nome_barato}.')
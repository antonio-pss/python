viagem = float(input('Qual é a distância da viagem? '))
if viagem > 200:
    print(f'O preço da passagem é R${viagem*0.45:.2f}')
else:
    print(f'O preço da passagem é R${viagem*0.50:.2f}')
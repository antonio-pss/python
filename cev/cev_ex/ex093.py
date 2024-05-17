jogador = {'Nome':[], 'Gols':[], 'Total':[0]}
jogador['Nome'].append(str(input('Nome: ')))
jogos = int(input('Quantos jogo ele jogou? '))

for i in range(jogos):
    jogador['Gols'].append(int(input(f'Jogo {i+1}: ')))
    jogador['Total'][0] += jogador['Gols'][i]

print(jogador)

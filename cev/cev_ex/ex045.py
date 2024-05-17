from random import choice

escolhas = ['Pedra', 'Papel', 'Tesoura']
jogador = str(input('Vamos jogar pedra, papel e tesoura. Qual sua escolha? ')).capitalize().strip()
computador = choice(escolhas)

if jogador == computador:
    print(f'Você empataram! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Pedra' and computador == 'Papel':
    print(f'Você perdeu! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Pedra' and computador == 'Tesoura':
    print(f'Você ganhou! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Papel' and computador == 'Tesoura':
    print(f'Você perdeu! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Papel' and computador == 'Pedra':
    print(f'Você ganhou! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Tesoura' and computador == 'Pedra':
    print(f'Você perdeu! Você escolheu {jogador} e o computador escolheu {computador}.')
elif jogador == 'Tesoura' and computador == 'Papel':
    print(f'Você ganhou! Você escolheu {jogador} e o computador escolheu {computador}.')
else:
    print('Você digitou errado...')
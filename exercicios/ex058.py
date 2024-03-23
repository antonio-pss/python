from random import randint
computador = randint(0, 10)
jogador = -1
palpites = 0

print('Tente adivinhar o número de 1 a 10 que o computador pensou.')

while (jogador != computador):
    jogador = int(input('Sua escolha: '))
    if jogador < computador:
        print('Mais...tente mais uma vez.')
    elif jogador > computador:
        print('Menos...tente mais uma vez.')
    else:
        print('Parabéns, você acertou.')
    palpites += 1


print(f'Você tentou {palpites} vezes.')

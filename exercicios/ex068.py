from random import randint

pontosJ = 0

while True:
    escolha = 0
    computador = randint(0, 10)
    jogador = -1
    while True:
        if escolha != 1 and escolha != 2:
            escolha = int(input('Sua escolha é Ímpar(1) ou Par(2): '))
        else:
            break

    while True:
        if jogador < 0 or jogador > 10:
            jogador = int(input('Escreva o número de dedos (0 a 10): '))
        else:
            break

    if escolha == 1:
        if (computador+jogador) % 2 == 0:
            print(f'Você perdeu!!! Você jogou {jogador} e o computador {computador}, que dá {jogador+computador}, que é par.')
            break
        else:
            print(f'Você ganhou!!! Você jogou {jogador} e o computador {computador}, que dá {jogador+computador}, que é ímpar.')
            pontosJ += 1
    elif escolha == 2:
        if (computador+jogador) % 2 != 0:
            print(f'Você perdeu!!! Você jogou {jogador} e o computador {computador}, que dá {jogador+computador}, que é ímpar.')
            break
        else:
            print(f'Você ganhou!!! Você jogou {jogador} e o computador {computador}, que dá {jogador+computador}, que é par.')
            pontosJ += 1

print(f'Você ganhou {pontosJ} vezes.')

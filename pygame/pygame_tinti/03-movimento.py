import sys
import pygame

pygame.init()  # Inicializa todos os atributos e funções do PyGames.

largura = 640
altura = 480

x = y = 0  # Ajudantes para fazer a movimentação dos draws.

tela = pygame.display.set_mode((largura, altura))  # Cria a tela do jogo.
pygame.display.set_caption('Jogo')  # Nome da janela.
clock = pygame.time.Clock()  # Frames do jogo.

while True:  # Para que o jogo funcione ele precisa estar rodando em um loop infinito.

    clock.tick(60)  # A quantos frames o jogo irá rodar.
    tela.fill((0, 0, 0))  # A tela é preenchida com preto a cada loop.

    for event in pygame.event.get():  # Fica procurando novos eventos.
        if event.type == pygame.QUIT:
            pygame.quit()  # Para o jogo.
            sys.exit()  # Fecha a janela.

    pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 40))  # Desenhar um retângulo na tela.
    # 1º Onde, 2º Cor, 3ª Posição.

    if y >= altura:
        y = 0
    if x >= largura:
        x = 0

    y += 1

    pygame.display.update()  # Atualiza o jogo para que ele não fique travado.

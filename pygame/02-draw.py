import sys
import pygame
from pygame.locals import *

pygame.init()  # Inicializa todos os atributos e funções do PyGames.

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))  # Cria a tela do jogo.
pygame.display.set_caption('Jogo')  # Nome da janela.

while True:  # Para que o jogo funcione ele precisa estar rodando em um loop infinito.
    for event in pygame.event.get():  # Fica procurando novos eventos.
        if event.type == QUIT:
            pygame.quit()  # Para o jogo.
            sys.exit()  # Fecha a janela.

    pygame.draw.rect(tela, (0, 255, 0), (200, 300, 40, 40))  # Desenhar um retângulo na tela.
    # O primeiro parâmetro é onde será desenhado.
    # O segundo é uma tupla com cores RGB.
    # O terceiro é uma tupla com a posição x e y do retângulo e largura e altura.

    pygame.draw.circle(tela, (255, 0, 0), (100, 200),40)  # Desenhar um círculo na tela.
    # 1º Onde, 2º Cor, 3º Onde, 4° Raio.

    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)  # Desenhar uma linha.
    # 1º Onde, 2º Cor, 3º Início, 4º Fim, 5º Espessura.

    

    pygame.display.update()  # Atualiza o jogo para que ele não fique travado.

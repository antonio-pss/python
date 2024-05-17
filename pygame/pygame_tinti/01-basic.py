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
    pygame.display.update()  # Atualiza o jogo para que ele não fique travado.

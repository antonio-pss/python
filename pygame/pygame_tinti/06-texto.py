import sys
import pygame
from random import randint

pygame.init()  # Inicializa todos os atributos e funções do PyGames.

largura = 640
altura = 480

x = y = 0  # Ajudantes para fazer a movimentação dos draws.
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
# 1º Tipo, 2º Tamanho, 3º Negrito, 4º Itálico

tela = pygame.display.set_mode((largura, altura))  # Cria a tela do jogo.
pygame.display.set_caption('Jogo')  # Nome da janela.
clock = pygame.time.Clock()  # Frames do jogo.

while True:  # Para que o jogo funcione ele precisa estar rodando em um loop infinito.

    clock.tick(60)  # A quantos frames o jogo irá rodar.
    tela.fill((0, 0, 0))  # A tela é preenchida com preto a cada loop.

    mensagem = f'Pontos {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))

    for event in pygame.event.get():  # Fica procurando novos eventos.
        if event.type == pygame.QUIT:
            pygame.quit()  # Para o jogo.
            sys.exit()  # Fecha a janela.

    if pygame.key.get_pressed()[pygame.K_a]:
        x = x - 10
    elif pygame.key.get_pressed()[pygame.K_d]:
        x = x + 10
    elif pygame.key.get_pressed()[pygame.K_w]:
        y = y - 10
    elif pygame.key.get_pressed()[pygame.K_s]:
        y = y + 10

    ret_verde = pygame.draw.rect(tela, (0, 255, 0), (x, y, 40, 40))  # Desenhar um retângulo na tela.
    # 1º Onde, 2º Cor, 3ª Posição.
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 40))

    if ret_verde.colliderect(ret_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()  # Atualiza o jogo para que ele não fique travado.

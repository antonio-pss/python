import sys
import pygame
from random import randint

pygame.init()  # Inicializa todos os atributos e funções do PyGames.

pygame.mixer.music.load('sons/Marimba Chill - Jimena Contreras.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

barulho_collision = pygame.mixer.Sound('sons/smw_1-up.wav')

largura = 640
altura = 480

x_snake = y_snake = 0  # Ajudantes para fazer a movimentação dos draws.
x_apple = randint(40, 600)
y_apple = randint(50, 430)

velocidade = 10
x_controle = 0
y_controle = velocidade

lista_snake = []
comprimento_inicial = 5

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)
# 1º Tipo, 2º Tamanho, 3º Negrito, 4º Itálico

tela = pygame.display.set_mode((largura, altura))  # Cria a tela do jogo.
pygame.display.set_caption('Jogo')  # Nome da janela.
clock = pygame.time.Clock()  # Frames do jogo.

morreu = False


def aumenta_snake(head):
    for XeY in head:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_snake, morreu
    pontos = 0
    comprimento_inicial = 5
    x_snake = y_snake = 0
    lista_snake = []
    morreu = False


while True:  # Para que o jogo funcione ele precisa estar rodando em um loop infinito.

    clock.tick(30)  # A quantos frames o jogo irá rodar.
    tela.fill((255, 255, 255))  # A tela é preenchida com preto a cada loop.

    mensagem = f'Pontos {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():  # Fica procurando novos eventos.
        if event.type == pygame.QUIT:
            pygame.quit()  # Para o jogo.
            sys.exit()  # Fecha a janela.

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and not x_controle == velocidade:
                x_controle = -velocidade
                y_controle = 0
            elif event.key == pygame.K_d and not x_controle == -velocidade:
                x_controle = velocidade
                y_controle = 0
            elif event.key == pygame.K_w and not y_controle == velocidade:
                x_controle = 0
                y_controle = -velocidade
            elif event.key == pygame.K_s and not y_controle == - velocidade:
                x_controle = 0
                y_controle = velocidade

    x_snake += x_controle
    y_snake += y_controle

    snake = pygame.draw.rect(tela, (0, 255, 0), (x_snake, y_snake, 20, 20))  # Desenhar um retângulo na tela.
    # 1º Onde, 2º Cor, 3ª Posição.
    apple = pygame.draw.rect(tela, (255, 0, 0), (x_apple, y_apple, 20, 20))

    if snake.colliderect(apple):
        x_apple = randint(40, 600)
        y_apple = randint(50, 430)
        pontos += 1
        barulho_collision.play()
        comprimento_inicial += 1

    lista_head = [x_snake, y_snake]
    lista_snake.append(lista_head)

    if lista_snake.count(lista_head) > 1:
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = 'Game Over! Pressione R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255, 255, 255))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_snake > largura:
        x_snake = 0
    if x_snake < 0:
        x_snake = largura
    if y_snake < 0:
        y_snake = altura
    if y_snake > altura:
        y_snake = 0

    if len(lista_snake) > comprimento_inicial:
        del lista_snake[0]

    aumenta_snake(lista_snake)

    tela.blit(texto_formatado, (450, 40))

    pygame.display.update()  # Atualiza o jogo para que ele não fique travado.

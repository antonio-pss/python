# PARA O QUE USAMOS O PYGAME?
# O PyGame serve essencialmente para 3 coisas:
# Criar imagens (draw) e tocar sous (mixer);
# Checar o que o jogador irá digitar;
# Outras coisas de desenvolvimento, como colisão.

# POR QUE APRENDER PYGAME?
# Utilizar o PyGame em vez de uma engine faz você resolver problemas você mesmo.
# No fim, isso faz você se tornar um bom programador e, se precisar, aprender outras coisas rapidamente.
# Com uma engine, você fica preso a ela.

import pygame
import sys

pygame.init()  # Inicía o PyGame e o deixa fazer tudo o que tem para fazer.
# Essencialmente, ele liga o 'motor' do jogo/biblioteca, nos dando suas funcionalidades.

width = 800  # Largura da tela.
height = 400  # Tamanho da tela.

screen = pygame.display.set_mode((width, height))  # Cria a tela do jogo e adiciona em uma variável.
# Como parâmetros, o set_mode recebe uma tupla com a largura e altura da tela.
# Estes dois parâmetros serão os pixels que sua tela terá.
# É interessante usar variáveis para adicionar a largura e altura da tela. Fica mais fácil de manipular no código.

pygame.display.set_caption('PyGame Guide')  # Cria o nome da tela.

# Um jogo tem o que chamamos de 'frame rate' ou taxa de quadros.
# Vamos dizer que você tem um personagem se movendo 10 pixels por quadro.
# Então se você tem 1 quadro por segundo, ele se movimentará 10 pixels por segundo.
# Se você tem 100 quadros por segundo, ele se movimentará 1000 pixels por segundo.
# O ideal é rodar nosso jogo a 60 quadros por segundo.

clock = pygame.time.Clock()  # Aqui criamos um objeto 'Clock', ele ajustará o frame rate do jogo.

# SURFACES OU SUPERFÍCIES.
# No PyGame, colocamos os objetos em 'Surfaces', superfícies. Temos duas delas:
# Display Surface: A tela do jogo.
# Regular Surface: Alguma imagem, cor ou texto. Precisa ser colocada em cima da Display Surface.

# SUPERFÍCIE SIMPLES.
# test_surface = pygame.Surface((100, 200))  # Criando uma superfície.
# test_surface.fill('Red')  # Aqui preenchemos a superfície com alguma cor.
# Essa cor é dada por um código RPG em uma tupla. Ex: (255, 255, 255).
# Ou você pode dar uma string com o nome da cor em inglês. Ex: 'White'.

# SUPERFÍCIE COM IMAGEM.
background_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/Ground.png').convert()
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()

# FUNÇÃO CONVERT() e CONVERT_ALPHA()
# Servem para mudar o tipo da variável em algo mais fácil de ultilizar pelo pygame.
# Básicamente fazem o jogo rodar melhor.

# CRIANDO TEXTO.
# Primeiros temos que criar o estilo da fonte.
# Colocamos esse texto em uma superfície e então adicionamos essa superfície no código com blit.
score_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # Aqui temos qual fonte será e o tamanho.
score_surface = score_font.render('Points: ', True, 'Black')
# 1º Parâmetro == Texto, 2º Antialias (False or True), 3º Cor.
# O Antialias é para deixar o texto mais 'redondo'.

# RECTS - Pode ser criado com pygame.Rect(left, top, width, height)
# Colocar as superfícies mais precisamente; Detectar colisões; Desenhar com pygame.draw().
snail_rect = snail_surface.get_rect(bottomleft=(800, 300))
player_rect = player_surface.get_rect(bottomleft=(100, 300))
score_rect = score_surface.get_rect(topright=(750, 50))


# LOOP INFINITO:
while True:  # Para que o jogo rode, é necessário um loop infinito.
    # Dentro do loop vamos:
    # Criar todos nossos elementos.
    # Atualizar tudo enquanto o jogo roda.

    # TRATAMENTO DE EVENTOS.
    for event in pygame.event.get():  # Vamos pegar uma variável 'event' em uma lista de eventos.
        # Esses eventos irão acontecer com os 'inputs' do jogador.
        if event.type == pygame.QUIT:  # Aqui verificamos se o tipo do evento que ocorreu foi uma saída.
            pygame.quit()  # Essa linha é o oposto da linha pygame.init().
            # Isso faz o 'motor' parar. Nos tirando várias funções e desligando o jogo.
            # Mas o código continua mesmo após deligar o pygame.
            # Dará um erro se o código continuar.
            sys.exit()  # Para fechar o código, precisamos dessa linha.

        # if event.type == pygame.MOUSEMOTION and player_rect.collidepoint(event.pos):

    # As superfícies seguem uma hierarquia, quem é criada primeiro fica mais fundo na tela.
    screen.blit(background_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.draw.rect(screen, 'Pink', score_rect)
    screen.blit(score_surface, score_rect)

    snail_rect.x -= 3  # Ficará rodando fazendo com que o 'snail' ande para esquerda.
    if snail_rect.right < 0:  # Se o 'snail' passar da borda esquerda da tela.
        snail_rect.x = 800  # Ele volta para direita.
    screen.blit(snail_surface, snail_rect)  # Faz com que a posição da 'surface' seja a mesma da 'rect'.
    screen.blit(player_surface, player_rect)  # Ajudando a mover a surface e nos dando possibilidade de colisão.
    # O comando blit básicamente diz que iremos colocar uma superfície em cima da outra.
    # Chamamos o comando com a superfície que irá ficar em baixo.
    # E damos como parâmetro a superfície que irá ficar em cima e onde ficará.
    # Quando colocamos algo na tela sem específicar, o x e y sempre será na parte superior esquerda.

    # if player_rect.colliderect(snail_rect):  # Função de colisão com rects: 'rect1.colliderect(rect2)'. Retorna bool.
        # Isso rodará todas às vezes que eles colidirem no frame. Podendo ser mais de 60.
        # Para um jogo com pontos de vida, pode ser um problema, mas com uma só vida não tem problema.
        # Já que apos a primeira colisão vai parar o jogo.

    # mouse_pos = pygame.mouse.get_pos()  # Pegando a posição x e y do mouse, devolvendo uma tupla (x, y)
    # if player_rect.collidepoint(mouse_pos):

    pygame.display.update()  # Aqui estamos atualizando a tela.
    clock.tick(60)  # Usamos nosso objeto clock para indicar os frame rate, no caso 60.

# DETALHES QUE NÃO SOUBE ONDE COLOCAR:
# ---------------------------------------------------------------------------------------------------------------------
# PLANO CARTESIANO DA TELA:
# A tela começa no canto superior esquerdo.
# Quando aumentamos o Y da tela, vamos para baixo.
# Quando aumentos o X, vamos para direita normalmente.
# (0, 0)
# |-------> X
# |
# ↓ -> Y

# RECTS POSITION.
# top, mid, bottom
# left, mid, right

# POSIÇÃO DO MOUSE: posição, clicks, visível e outros...
# Com pygame.mouse:
# Com pygame.mouse.get_pos() - Devolve uma tupla com posição x e y = (x, y).
# Com pygame.mouse.get_pressed() - Devolve uma tupla com bool = (false, false, false) Botão esquerdo, meio e direito.

# Com event loop:
# if event.type == pygame.MOUSEMOTION:
# if event.type == pygame.MOUSEBUTTON...:

# EVENTS:
# event.type
# event.pos = Onde o evento está ocorrendo.

# PYGAME.DRAW():
# Draw rects, circles, lines, pointes, ellipses...

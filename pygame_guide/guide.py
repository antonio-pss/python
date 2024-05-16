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
height = 300  # Tamanho da tela.

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
background = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/Ground.png')

# CRIANDO TEXTO.
# Primeiros temos que criar o estilo da fonte.
# Colocamos esse texto em uma superfície e então adicionamos essa superfície no código com blit.
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)  # Aqui temos qual fonte será e o tamanho.
text = test_font.render('Points: ', True, 'Black')
# 1º Parâmetro == Texto, 2º Antialias (False or True), 3º Cor.
# O Antialias é para deixar o texto mais 'redondo'.


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

    # As superfícies seguem uma hierarquia, quem é criada primeiro fica mais fundo na tela.
    screen.blit(background, (0, 0))
    screen.blit(ground, (0, 250))
    screen.blit(text, (625, 25))
    # O comando blit básicamente diz que iremos colocar uma superfície em cima da outra.
    # Chamamos o comando com a superfície que irá ficar em baixo.
    # E damos como parâmetro a superfície que irá ficar em cima e onde ficará.
    # Quando colocamos algo na tela sem específicar, o x e y sempre será na parte superior esquerda.

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

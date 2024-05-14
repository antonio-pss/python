import pygame
import sys

pygame.init()

window = pygame.display.set_mode((400, 200))  # Tamanho tela.
pygame.display.set_caption('Sprites')  # Nome da tela.


class Frog(pygame.sprite.Sprite):  # Criando um sprite como classe.
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Inicializar a super.
        self.sprites = []
        self.sprites.append(pygame.image.load('sprites\\attack_1.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_2.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_3.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_4.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_5.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_6.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_7.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_8.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_9.png'))
        self.sprites.append(pygame.image.load('sprites\\attack_10.png'))
        self.current = 0
        self.image = self.sprites[self.current]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))

        self.rect = self.image.get_rect()
        self.rect.bottomleft = 0, 200

        self.animate = False

    def update(self):
        if self.animate:
            self.current += 0.2
            if self.current >= len(self.sprites):
                self.current = 0
                self.animate = False

            self.image = self.sprites[int(self.current)]
            self.image = pygame.transform.scale(self.image, (128*3, 64*3))

    def attack(self):
        self.animate = True


all_sprites = pygame.sprite.Group()
frog = Frog()

all_sprites.add(frog)

clock = pygame.time.Clock()

while True:  # Loop principal do jogo.
    window.fill((0, 0, 0))  # Cor da tela.
    clock.tick(60)

    for event in pygame.event.get():  # Eventos.
        if event.type == pygame.QUIT:  # Evento de saída.
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            frog.attack()

    all_sprites.draw(window)
    all_sprites.update()

    pygame.display.flip()



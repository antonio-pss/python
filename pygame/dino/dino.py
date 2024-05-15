from random import randrange
import pygame
import sys
import os


direct_principal = os.path.dirname(__file__)  # Caminho absoluto onde o script está.
direct_images = os.path.join(direct_principal, 'images')
direct_sounds = os.path.join(direct_principal, 'sounds')

window = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Dino Game')

sprite_sheet = pygame.image.load(os.path.join(direct_images, 'dinoSpritesheet.png')).convert_alpha()


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images_dino = []
        for i in range(3):
            img = sprite_sheet.subsurface((i*32, 0), (32, 32))
            img = pygame.transform.scale(img, (32*2, 32*2))
            self.images_dino.append(img)

        self.index = 0
        self.image = self.images_dino[self.index]
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (100, 450)

    def update(self):
        if self.index > 2:
            self.index = 0
        self.index += 0.25
        self.image = self.images_dino[int(self.index)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32 * 7, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32 * 2, 32 * 2))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 32)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = 1000 - randrange(30, 300, 90)
            self.rect.y = randrange(50, 200, 32)
        self.rect.x -= 10


class Floor(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((32*6, 0), (32, 32))
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.center = (x*64, 442)

    def update(self):
        if self.rect.bottomright[0] < 0:
            self.rect.center = (640 + 32*2, 442)
        self.rect.x -= 10


sprites = pygame.sprite.Group()

dino = Dino()
sprites.add(dino)

for i in range(4):
    nuvem = Nuvens()
    sprites.add(nuvem)

for i in range(12):
    floor = Floor(i)
    sprites.add(floor)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sprites.draw(window)
    sprites.update()

    pygame.display.flip()

import pygame
import sys
from random import randint
from os.path import join


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(join('graphics', 'tree.png')).convert_alpha()
        self.rect = self.image.get_frect(topleft=pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(join('graphics', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=pos)
        self.direction = pygame.Vector2()
        self.speed = 300

    def input(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.y = keys[pygame.K_s] - keys[pygame.K_w]
        self.direction.x = keys[pygame.K_d] - keys[pygame.K_a]
        self.rect.center += self.direction * self.speed * delta

    def update(self, dt):
        self.input(delta)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        self.offset = pygame.Vector2()

        self.ground_surf = pygame.image.load(join('graphics', 'ground.png')).convert_alpha()
        self.ground_rect = self.ground_surf.get_frect(topleft=(0, 0))

    def custom_draw(self):
        ground_offset = self.ground_rect.topleft + self.offset
        self.display_surface.blit(self.ground_surf, self.ground_rect)
        for sprite in sorted(self.sprites(), key=lambda spt: spt.rect.centery):
            offset_pos = sprite.rect.topleft + self.offset
            self.display_surface.blit(sprite.image, sprite.rect)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

camera_group = CameraGroup()
Player((640, 360), camera_group)

for i in range(20):
    x = randint(0, 1000)
    y = randint(0, 1000)
    Tree((x, y), camera_group)

while True:
    delta = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#71ddee')

    camera_group.update(delta)
    camera_group.custom_draw()

    pygame.display.update()

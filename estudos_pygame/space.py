import pygame
from os.path import join
from random  import randint


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('Space Shooter', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.direction = pygame.math.Vector2()
        self.speed = 300

    def movement(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * self.speed * delta

    def update(self):
        self.movement()


# General Setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()
running = True

# Sprites
all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


# Stars
star_surf = pygame.image.load(join('Space Shooter', 'images', 'star.png')).convert_alpha()
star_positions = [(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)) for i in range(20)]

# Meteors
meteor_surf = pygame.image.load(join('Space Shooter', 'images', 'meteor.png')).convert_alpha()
meteor_rect = meteor_surf.get_frect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

# Laser
laser_surf = pygame.image.load(join('Space Shooter', 'images', 'laser.png')).convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft=(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20))

while running:
    # Frame Rate
    delta = clock.tick(60) / 1000
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Screen
    screen.fill('darkgray')
    for pos in star_positions:
        screen.blit(star_surf, pos)

    screen.blit(meteor_surf, meteor_rect)
    screen.blit(laser_surf, laser_rect)
    all_sprites.draw(screen)

    # Configurations
    pygame.display.update()

# Over
pygame.quit()

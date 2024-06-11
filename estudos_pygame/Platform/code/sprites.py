from settings import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(topleft=pos)


class Player(Sprite):
    def __init__(self, pos, groups, collision_sprites):
        surf = pygame.Surface((40, 80))
        super().__init__(pos, surf, groups)

        # movement & collision
        self.direction = pygame.Vector2(0, 0)
        self.collision_sprites = collision_sprites
        self.speed = 400

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = keys[pygame.K_d] - keys[pygame.K_a]
        self.direction.y = keys[pygame.K_s] - keys[pygame.K_w]

    def move(self, delta):
        self.rect.x += self.direction.x * self.speed * delta
        self.collision('horizontal')
        self.rect.y += self.direction.y * self.speed * delta
        self.collision('vertical')

    def collision(self, direction):
        pass

    def update(self, delta):
        self.input()
        self.move(delta)

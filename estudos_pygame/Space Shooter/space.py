import pygame
from os.path import join
from random import randint, uniform


class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

        # Movement
        self.direction = pygame.Vector2()
        self.speed = 500

        # Cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.laser_cooldown_duration = 400

    def movement(self):
        keys = pygame.key.get_pressed()
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_w])
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_a])
        self.direction = self.direction.normalize() if self.direction else self.direction

        self.rect.center += self.direction * self.speed * delta

    def shoot(self):
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_sprites, laser_surface, self.rect.midtop)
            laser_sound.play()
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()

        # Shoot Cooldown.
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.laser_cooldown_duration:
                self.can_shoot = True

    def update(self):
        self.movement()
        self.shoot()


class Star(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, SCREEN_WIDTH), randint(0, SCREEN_HEIGHT)))


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)

    def update(self):
        self.rect.centery -= 750 * delta
        self.leave()

    def leave(self):
        if self.rect.bottom <= 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.original_image = meteor_surface
        self.image = self.original_image
        self.rect = self.image.get_frect(midbottom=(randint(0, SCREEN_WIDTH), 0))

        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = 400

        self.life_time = 2000
        self.start_time = pygame.time.get_ticks()

        self.rotation = 0
        self.rotation_speed = randint(0, 100)

    def update(self):
        self.movement()
        self.destroy()
        self.rotation += self.rotation_speed * delta
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def movement(self):
        self.rect.center += self.direction * self.speed * delta

    def destroy(self):
        if pygame.time.get_ticks() - self.start_time >= self.life_time:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, groups, frames, pos):
        super().__init__(groups)
        self.frames = frames
        self.frame_index = 0
        self.image = frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        self.frame_index += 30 * delta
        if self.frame_index < len(self.frames):
            self.image = self.frames[int(self.frame_index)]
        else:
            self.kill()


def collisions():
    global running
    if pygame.sprite.spritecollide(player, meteor_sprites, False, pygame.sprite.collide_mask):
        running = False

    for laser in laser_sprites:
        if pygame.sprite.spritecollide(laser, meteor_sprites, True, pygame.sprite.collide_mask):
            laser.kill()
            Explosion(all_sprites, explosion_frames, laser.rect.midtop)


def display_score():
    current_time = pygame.time.get_ticks() // 100
    score_surface = font.render(f'{current_time}', True, (240, 240, 240))
    score_rect = score_surface.get_rect(midbottom=(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 50))
    screen.blit(score_surface, score_rect)
    pygame.draw.rect(screen, (240, 240, 240), score_rect.inflate(20, 15).move(0, -5), 3, 10)


# General Setup
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Shooter')
clock = pygame.time.Clock()
running = True
# pygame.mixer.Sound(join('audio', ''))

# Imports (Surfaces, Font, Sounds)
star_surface = pygame.image.load(join('images', 'star.png'))
laser_surface = pygame.image.load(join('images', 'laser.png'))
meteor_surface = pygame.image.load(join('images', 'meteor.png'))
font = pygame.font.Font(join('images', 'Oxanium-Bold.ttf'), 30)

laser_sound = pygame.mixer.Sound(join('audio', 'laser.wav'))
laser_sound.set_volume(0.1)


# Explosion
explosion_frames = [pygame.image.load(join('images', 'explosion', f'{i}.png')).convert_alpha() for i in range(21)]

# Sprites
all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()
for i in range(10):
    Star(all_sprites, star_surface)
player = Player(all_sprites)

# Timer
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500)

while running:
    # Frame Rate
    delta = clock.tick(60) / 1000
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == meteor_event:
            Meteor(meteor_sprites)

    # Draw
    screen.fill('#3a2e3f')
    display_score()
    all_sprites.draw(screen)
    meteor_sprites.draw(screen)
    laser_sprites.draw(screen)

    # Update
    all_sprites.update()
    meteor_sprites.update()
    laser_sprites.update()
    collisions()

    # Configurations
    pygame.display.update()

# Over
pygame.quit()

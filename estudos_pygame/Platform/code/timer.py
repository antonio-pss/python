import pygame.time

from settings import *


class Timer:
    def __init__(self, duration, func=None, repeat=None, autostart=False):
        self.duration = duration
        self.star_time = 0
        self.active = False
        self.func = func
        self.repeat = re

        if autostart:
            self.activate()

    def activate(self):
        self.active = True
        self.star_time = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.star_time = 0

    def update(self):
        if pygame.time.get_ticks() - self.star_time >= self.duration:
            if self.func and self.star_time != 0:
                self.func()
            self.deactivate()


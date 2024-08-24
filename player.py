import time

import pygame
from pygame import Mask, Surface, Rect
from pygame.sprite import Sprite, Group

import game_settings as s

class Bird(Sprite):
    def __init__(self, screen: Surface, bird_group: Group,
                 pipe_group: Group) -> None:
        super().__init__()

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/circle.png") \
        .convert_alpha()
        self.mask: Mask = pygame.mask.from_surface(self.image)
        self.rect: Rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 100

        self.y: float = float(self.rect.centery)

        bird_group.add(self)
        self.pipe_group: Group = pipe_group


    def update(self) -> None:
        if self.rect.top == 0 and (time.time()-s.last_touched) > 0.1: 
            s.touching_ceiling = True
            s.last_touched = time.time()

        if s.gravity > 0 and self.rect.bottom <= self.screen_rect.bottom:
            self.y += s.gravity
            self.rect.centery = self.y
        elif s.gravity <= 0 and 0 <= self.rect.top:
            self.y += s.gravity
            self.rect.centery = self.y

        self.check_collisions()

 
    def check_collisions(self) -> None:
        if pygame.sprite.spritecollide(self, self.pipe_group, False):
            if pygame.sprite.spritecollide(self, self.pipe_group, False,
                                           pygame.sprite.collide_mask):
                print("collided")


    def draw_bird(self) -> None:
        self.screen.blit(self.image, self.rect)

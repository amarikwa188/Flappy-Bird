import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

import game_settings as s


class Pipe(Sprite):
    def __init__(self, screen: Surface, pipe_group: Group,
                 size: int=0, orientation: int=0) -> None:
        super().__init__()

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/pipe.png")\
            .convert_alpha()
        self.mask: Mask = pygame.mask.from_surface(self.image)
        self.rect: Rect = self.image.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        self.rect.left = self.screen_rect.right

        pipe_group.add(self)

        self.x: float = float(self.rect.centerx)


    def update(self) -> None:
        self.x -= s.bg_speed
        self.rect.centerx = self.x

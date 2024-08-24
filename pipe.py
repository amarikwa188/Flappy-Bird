import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

import game_settings as s

from typing import Literal


class Pipe(Sprite):
    def __init__(self, screen: Surface, pipe_group: Group,
                 size: Literal[1,2,3], orientation: Literal[0,1]) -> None:
        super().__init__()

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = self.set_sprite(size)
        self.mask: Mask = pygame.mask.from_surface(self.image)

        self.rect: Rect = self.image.get_rect()
        self.rect.left = self.screen_rect.right

        self.set_orientation(orientation)

        pipe_group.add(self)

        self.x: float = float(self.rect.centerx)


    def update(self) -> None:
        self.x -= s.bg_speed
        self.rect.centerx = self.x


    def set_sprite(self, size) -> Surface:
        match size:
            # set sprite image
            case 1:
                # small
                return pygame.image.load("sprites/pipe_s.png").convert_alpha()
            case 2:
                # medium
                return pygame.image.load("sprites/pipe_m.png").convert_alpha()
            case 3:
                # large
                return pygame.image.load("sprites/pipe_l.png").convert_alpha()
        
        raise ValueError(f"Invalid pipe size: {size}")
            

    def set_orientation(self, orientation) -> None:
        match orientation:
            case 0:
                # bottom
                self.rect.bottom = self.screen_rect.bottom
            case 1:
                # top
                self.image = pygame.transform.rotate(self.image, 180)
                self.rect.top = self.screen_rect.top
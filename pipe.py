import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group


class Pipe(Sprite):
    def __init__(self, screen: Surface, pipe_group: Group) -> None:
        super().__init__()

        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/pipe.png")\
            .convert_alpha()
        self.mask: Mask = pygame.mask.from_surface(self.image)
        self.rect: Rect = self.image.get_rect()

        pipe_group.add(self)

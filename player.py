import pygame
from pygame import Mask, Surface, Rect
from pygame.sprite import Sprite, Group

class Bird:
    def __init__(self, screen: Surface) -> None:
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        self.image: Surface = pygame.image.load("sprites/circle.png") \
        .convert_alpha()
        self.rect: Rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center


    def draw_bird(self) -> None:
        self.screen.blit(self.image, self.rect)

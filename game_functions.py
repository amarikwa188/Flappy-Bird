import sys

import pygame
from pygame import Surface

import game_settings as s


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_screen(screen: Surface) -> None:
    screen.fill(s.bg_color)
    pygame.display.flip()
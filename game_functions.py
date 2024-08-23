import sys
import time
from threading import Thread

import pygame
from pygame import Surface
from pygame.event import Event

import game_settings as s

from player import Bird


def check_events() -> None:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def check_keydown_events(event: Event) -> None:
    if event.key == pygame.K_SPACE:
        print("fly") 


def update_screen(screen: Surface, player: Bird) -> None:
    screen.fill(s.bg_color)
    player.draw_bird()
    pygame.display.flip()
import sys
import time
from threading import Thread

import pygame
from pygame import Surface
from pygame.sprite import Group
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
    if event.key == pygame.K_SPACE and not s.flying:
        Thread(target=fly, daemon=True).start()


def fly() -> None:
    s.flying = True
    original_gravity: float = s.gravity
    upward_force: float = 0.5

    while upward_force > 0:
        if s.touching_ceiling:
            s.touching_ceiling = False
            break
        
        s.gravity = -upward_force
        time.sleep(0.05)
        upward_force -= 0.1

    s.gravity = original_gravity   
    s.flying = False


def update_screen(screen: Surface, player: Bird, pipe_group: Group) -> None:
    screen.fill(s.bg_color)
    player.draw_bird()
    pipe_group.draw(screen)
    pygame.display.flip()
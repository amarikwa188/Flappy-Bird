import sys
import time
from threading import Thread

import pygame
from pygame import Surface
from pygame.sprite import Group
from pygame.event import Event

import game_settings as s

from player import Bird
from pipe import Pipe

from ui_handler import UIHandler


def check_events() -> None:
    """
    Handle user input.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)


def check_keydown_events(event: Event) -> None:
    """
    Handle key presses.

    :param event: the given input event.
    """
    if event.key == pygame.K_SPACE and not s.flying:
        Thread(target=fly, daemon=True).start()


def fly() -> None:
    """
    Handle player flight.
    """
    s.flying = True
    original_gravity: float = s.gravity
    upward_force: float = s.upward_force

    while upward_force > 0:
        if s.touching_ceiling:
            s.touching_ceiling = False
            break
        
        s.gravity = -upward_force
        time.sleep(0.05)
        upward_force -= 0.1

    s.gravity = original_gravity   
    s.flying = False


def clear_pipes(pipe_group: Group) -> None:
    """
    Delete pipes that have moved off the screen.

    :param pipe_group: a sprite group containing the pipes.
    """
    pipe_list: list[Pipe] = pipe_group.sprites()

    for pipe in pipe_list:
        if pipe.rect.right <= 0:
            pipe_group.remove(pipe)


def update_screen(screen: Surface, player: Bird, pipe_group: Group,
                  ui: UIHandler) -> None:
    """
    Update the screen.

    :param screen: the game screen.
    :param player: the player character.
    :param pipe_group: a sprite group containing the pipes.
    :param ui: a reference to the ui handler.
    """
    screen.fill(s.bg_color)
    player.draw_bird()
    pipe_group.draw(screen)
    ui.draw_ui()
    pygame.display.flip()
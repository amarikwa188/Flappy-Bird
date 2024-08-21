import pygame
from pygame import Surface

import game_functions as gf
import game_settings as s


def run_game() -> None:
    pygame.init()
    pygame.display.set_caption("Flappy Bird")

    screen: Surface = pygame.display.set_mode((s.screen_width,
                                               s.screen_height))

    while True:
        gf.check_events()
        gf.update_screen(screen)


if __name__ == "__main__":
    run_game()
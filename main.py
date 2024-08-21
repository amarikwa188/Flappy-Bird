import pygame
from pygame import Surface

import game_functions as gf


def run_game() -> None:
    pygame.init()
    pygame.display.set_caption("Flappy Bird")

    screen: Surface = pygame.display.set_mode((400,400))

    while True:
        gf.check_events()
        gf.update_screen()


if __name__ == "__main__":
    run_game()
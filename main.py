import pygame
from pygame import Surface
from pygame.sprite import Group

import game_functions as gf
import game_settings as s

from player import Bird


def run_game() -> None:
    pygame.init()
    pygame.display.set_caption("Flappy Bird")

    screen: Surface = pygame.display.set_mode((s.screen_width,
                                               s.screen_height))

    player_group: Group = Group()
    player: Bird = Bird(screen, player_group)

    while True:
        gf.check_events()
        player.update()
        gf.update_screen(screen, player)


if __name__ == "__main__":
    run_game()
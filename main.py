import pygame
from pygame import Surface
from pygame.sprite import Group

import game_functions as gf
import game_settings as s

from player import Bird
from pipe import Pipe


def run_game() -> None:
    pygame.init()
    pygame.display.set_caption("Flappy Bird")

    screen: Surface = pygame.display.set_mode((s.screen_width,
                                               s.screen_height))

    pipe_group: Group = Group()
    pipe: Pipe = Pipe(screen, pipe_group, 3, 0)

    player_group: Group = Group()
    player: Bird = Bird(screen, player_group, pipe_group)

    while True:
        gf.check_events()
        player.update()
        pipe_group.update()
        gf.update_screen(screen, player, pipe_group)


if __name__ == "__main__":
    run_game()
import time
from threading import Thread
import random as rng

from pygame import Surface
from pygame.sprite import Group

import game_settings as s

from ui_handler import UIHandler

from pipe import Pipe


class Spawner:
    def __init__(self, screen: Surface, pipe_group: Group,
                 ui: UIHandler) -> None:
        self.ui: UIHandler = ui

        self.screen: Surface = screen
        self.pipe_group: Group = pipe_group

        self.frequency: float = s.spawn_frequency

        Thread(target=self.spawn_pipes, daemon=True).start()


    def spawn_pipes(self) -> None:
        sizes: set[int] = {1,3}
        last_size: int =  0
        
        while True:
            size1: int = rng.choice(tuple(sizes - {last_size}))
            size2: int = (sizes - {size1}).pop()
            last_size = size1

            Pipe(self.screen, self.pipe_group, size1, 0, self.ui)
            Pipe(self.screen, self.pipe_group, size2, 1, self.ui)

            time.sleep(self.frequency)


import time
from threading import Thread
import random as rng

from pygame import Surface
from pygame.sprite import Group

import game_settings as s

from pipe import Pipe


class Spawner:
    def __init__(self, screen: Surface, pipe_group: Group) -> None:
        self.screen: Surface = screen
        self.pipe_group: Group = pipe_group

        self.frequency: float = s.spawn_frequency

        Thread(target=self.spawn_pipes, daemon=True).start()


    def spawn_pipes(self) -> None:
        while True:
            sizes: set[int] = {1,2,3}
            size1: int = rng.choice(tuple(sizes))
            size2: int =  rng.choice(tuple(sizes - {size1}))
            Pipe(self.screen, self.pipe_group, size1, 0)
            Pipe(self.screen, self.pipe_group, size2, 1)

            time.sleep(self.frequency)
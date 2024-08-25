import time
from threading import Thread
import random as rng

from pygame import Surface
from pygame.sprite import Group

import game_settings as s

from ui_handler import UIHandler

from pipe import Pipe


class Spawner:
    """Represents an instance of the pipe spawner."""
    def __init__(self, screen: Surface, pipe_group: Group,
                 ui: UIHandler) -> None:
        """
        Initializes a spawner object.

        :param screen: the game screen.
        :param pipe_group: a sprite group containing the pipes.
        :param ui: a reference to the ui handler.
        """
        # set up ui reference
        self.ui: UIHandler = ui

        # set up reference to the screen and pipe group
        self.screen: Surface = screen
        self.pipe_group: Group = pipe_group

        # the time in seconds between pipe spawns
        self.frequency: float = s.spawn_frequency

        # start the spawning thread
        Thread(target=self.spawn_pipes, daemon=True).start()


    def spawn_pipes(self) -> None:
        """
        Spawn a set of pipes at the top and bottom of the screen.
        """
        # the possible pipe sizes
        sizes: set[int] = {1,3}
        # track last size spawned to prevent repetition
        last_size: int =  0
        
        # spawn pipes
        while True:
            # choose two pipe sizes
            size1: int = rng.choice(tuple(sizes - {last_size}))
            size2: int = (sizes - {size1}).pop()
            last_size = size1

            # create pipe objects
            Pipe(self.screen, self.pipe_group, size1, 0, self.ui)
            Pipe(self.screen, self.pipe_group, size2, 1, self.ui)

            time.sleep(self.frequency)


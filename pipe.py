import pygame
from pygame import Surface, Rect, Mask
from pygame.sprite import Sprite, Group

import game_settings as s

from ui_handler import UIHandler

from typing import Literal


class Pipe(Sprite):
    """Represents an instance of the pipe obstacle."""
    def __init__(self, screen: Surface, pipe_group: Group,
                 size: Literal[1,2,3], orientation: Literal[0,1],
                 ui: UIHandler) -> None:
        """
        Initializes a pipe object.

        :param screen: the game screen.
        :param pipe_group: a sprite group that holds all pipes.
        :param size: represents the size of a pipe.
        :param orientation: whether the pipe is on the bottom(0) or top(1) of
        the screen.
        :param ui: a reference to the ui handler.
        """
        super().__init__()

        # set up screen reference
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # set up ui reference
        self.ui: UIHandler = ui

        # create sprite surface and mask for collisions
        self.image: Surface = self.set_sprite(size)
        self.mask: Mask = pygame.mask.from_surface(self.image)

        # position the pipe to the right off screen
        self.rect: Rect = self.image.get_rect()
        self.rect.left = self.screen_rect.right

        # set the orientation
        self.set_orientation(orientation)

        # add the pipe to the pipe group
        pipe_group.add(self)

        # a float value to handle smooth horizontal movement
        self.x: float = float(self.rect.centerx)


    def update(self) -> None:
        """
        Move the pipe to the left.
        """
        # move the pipe leftward
        self.x -= s.bg_speed
        self.rect.centerx = self.x

        # update the score
        if self.rect.centerx == self.screen_rect.centerx:
            self.ui.score += 0.05


    def set_sprite(self, size) -> Surface:
        """
        Set the correct sprite according to the size value.

        :param size: the size of the pipe.
        :return: the sprite surface.
        """
        match size:
            # set sprite image
            case 1:
                # small
                return pygame.image.load("sprites/pipe_s2.png").convert_alpha()
            case 2:
                # medium
                return pygame.image.load("sprites/pipe_m2.png").convert_alpha()
            case 3:
                # large
                return pygame.image.load("sprites/large_pipe.png").convert_alpha()
        
        raise ValueError(f"Invalid pipe size: {size}")
            

    def set_orientation(self, orientation) -> None:
        """
        Move the pipe to the top/bottom of the screen based on the
        orientation value.

        :param orientation: the orientation.
        """
        match orientation:
            case 0:
                # bottom
                self.rect.bottom = self.screen_rect.bottom
            case 1:
                # top
                self.image = pygame.transform.rotate(self.image, 180)
                self.rect.top = self.screen_rect.top
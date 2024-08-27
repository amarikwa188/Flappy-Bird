import sys
import time

import pygame
from pygame import Mask, Surface, Rect
from pygame.sprite import Sprite, Group

import game_settings as s


class Bird(Sprite):
    """Represents an instance of the player object."""
    def __init__(self, screen: Surface, bird_group: Group,
                 pipe_group: Group) -> None:
        """
        Initializes an instance of the player character.

        :param screen: the game screen.
        :param bird_group: a sprite group containing the player.
        :param pipe_group: a sprite group containing the pipes.
        """
        super().__init__()

        # set up screen reference
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # set the character sprite and create a mask for collisions
        self.image: Surface = pygame.image.load("sprites/circle.png") \
        .convert_alpha()
        self.mask: Mask = pygame.mask.from_surface(self.image)

        # position the character on the screen
        self.rect: Rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = 100

        # a float variable for handling smooth movement
        self.y: float = float(self.rect.centery)

        # add the object to the sprite group and create a reference to the
        # pipe group
        bird_group.add(self)
        self.pipe_group: Group = pipe_group


    def update(self) -> None:
        """
        Update the position of the player.
        """
        if self.rect.top == 0 and (time.time()-s.last_touched) > 0.1: 
            s.touching_ceiling = True
            s.last_touched = time.time()

        # apply gravity
        if s.gravity > 0 and self.rect.bottom <= self.screen_rect.bottom:
            self.y += s.gravity
            self.rect.centery = self.y
        elif s.gravity <= 0 and 0 <= self.rect.top:
            self.y += s.gravity
            self.rect.centery = self.y

        # check for collisions
        self.check_collisions()

 
    def check_collisions(self) -> None:
        """
        Check for collisions with obstacles.
        """
        # perform rect collision detection
        if pygame.sprite.spritecollide(self, self.pipe_group, False):
            # perform sprite collision detection
            if pygame.sprite.spritecollide(self, self.pipe_group, False,
                                           pygame.sprite.collide_mask):
                sys.exit()


    def draw_bird(self) -> None:
        """
        Draw the player to the screen.
        """
        self.screen.blit(self.image, self.rect)

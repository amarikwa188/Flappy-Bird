import pygame
from pygame import Surface, Rect
from pygame.font import Font


class UIHandler:
    """Represents an instance of the UI Manager."""
    def __init__(self, screen: Surface) -> None:
        """
        Inititalizes a ui handler object.

        :param screen: the game screen.
        """
        # set up game screen reference
        self.screen: Surface = screen
        self.screen_rect: Rect = self.screen.get_rect()

        # score font and value
        self.temp_font: Font = pygame.font.SysFont(None, 40)
        self.score: int = 0


    def draw_ui(self) -> None:
        """
        Draw the ui to the screen.
        """
        # display score
        image: Surface = self.temp_font.render(f"{round(self.score)}", True,
                                               (0,0,0))
        image_rect: Rect = image.get_rect()

        image_rect.x = image_rect.y = 0
        
        self.screen.blit(image, image_rect)
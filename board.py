import sys
import pygame
from pygame.locals import *

class Board:
    def __init__(self):
        WINDOW_SIZE = (600, 400)
        # create pygame window
        self._window = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        pygame.display.set_caption("Magma Boy and Hydro Girl")

import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        WINDOW_SIZE = (32 * 16, 24 * 16)
        # create pygame window
        self.screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
        pygame.display.set_caption("Magma Boy and Hydro Girl")

    def read_board_textures(path):
        '''
        Create a list containing the textures of the level.

        Each level map is made up of 24x32 chunks. Each chunk has a specfic
        texture. The different chunks types are mapped to unique integer
        values. All chunk data for a map is stored in a list of lists.

        Args:
            path::str
                path to txt file containing chunk data
        
        Returns:
            chunk_textures::[[...],[...],[...]]
                A list of lists which contain a integer value for every chunk
                in the level.
        '''
        chunk_textures = []

        with open(path) as f:
            for line in f:
                line = line.strip().split(',')  # convert string to list of str
                line = [int(chunk) for chunk in line]  # convert all str to in
                chunk_textures.append(line)

        return chunk_textures

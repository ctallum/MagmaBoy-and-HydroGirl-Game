import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self, path):
        """
        Args:
            path::str
                A path to a text file containing block placements
        """
        self.CHUNK_SIZE = 16
        self.load_map(path)
        self.load_images()
        self.make_solid_blocks()
        self.make_water_pools()
        self.make_lava_pools()
        self.make_goo_pools()

    def load_map(self, path):
        '''
        Create an array which contains the type of every chunk on the map.

        Each level map is made up of 24x32 chunks. Each type of chunk has
        specfic texture and properties. Each unique chunks type has a
        unique string value.

        Args:
            path::str
                path to txt file containing chunk data
        '''
        self._game_map = []

        with open(path) as f:
            for line in f:
                line = line.strip().split(',')  # convert string to list of str
                self._game_map.append(line)

    def get_game_map(self):
        """
        Return game map
        """
        return self._game_map

    def load_images(self):
        """
        Load all images needed to draw level background and platforms.

        Load in level background.Load all board chunk textures from local
        folder "data/board_textures and save textures in a dictionary.
        """
        self._background = pygame.image.load('data/board_textures/wall.png')
        # create dictionary that maps a string to a board texture
        self._board_textures = {
            "100": pygame.image.load('data/board_textures/100.png'),
            "100": pygame.image.load('data/board_textures/100.png'),
            "111": pygame.image.load('data/board_textures/111.png'),
            "112": pygame.image.load('data/board_textures/112.png'),
            "113": pygame.image.load('data/board_textures/113.png'),
            "114": pygame.image.load('data/board_textures/114.png'),
            "121": pygame.image.load('data/board_textures/121.png'),
            "122": pygame.image.load('data/board_textures/122.png'),
            "123": pygame.image.load('data/board_textures/123.png'),
            "124": pygame.image.load('data/board_textures/124.png'),
            "2": pygame.image.load('data/board_textures/lava.png'),
            "3": pygame.image.load('data/board_textures/water.png'),
            "4": pygame.image.load('data/board_textures/goo.png')
        }
        # set the colorkey for each image in dictionary
        for texture in self._board_textures.keys():
            self._board_textures[texture].set_colorkey((255, 0, 255))

    def get_background(self):
        """
        Return image of level background
        """
        return self._background

    def get_board_textures(self):
        """
        Return dictionary containing board images
        """
        return self._board_textures

    def make_solid_blocks(self):
        """
        Iterate through the map and make the walls and ground solid blocks
        which the player can collide with.
        """
        # create empty list to contain solid block rects
        CHUNKS_SIZE = 16
        self._solid_blocks = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if block is not air or a liquid
                if tile not in ['0', '2', '3', '4']:
                    # create a 16 x 16 rect and add it to the list
                    self._solid_blocks.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE,
                                    self.CHUNK_SIZE, self.CHUNK_SIZE))

    def get_solid_blocks(self):
        """
        Return a list of pygame rects that are solid.
        """
        return self._solid_blocks

    def make_lava_pools(self):
        """
        Create list containing lava pool rects
        """
        # create an empty list to store lava pool rects
        self._lava_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents lava
                if tile == "2":
                    # add a 16x8 rect to the list
                    self._lava_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_lava_pools(self):
        """
        Return list contaning lava pool rects
        """
        return self._lava_pools

    def make_water_pools(self):
        """
        Create list containing water pool rects
        """
        # Create empty list to store water pool rects
        self._water_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents water
                if tile == "3":
                    # add a 16x8 rect to the list
                    self._water_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_water_pools(self):
        """
        Return list containing water pool rects
        """
        return self._water_pools

    def make_goo_pools(self):
        """
        Create list containing goo pool rects
        """
        # create an empty list to store goo rects
        self._goo_pools = []
        for y, row in enumerate(self._game_map):
            for x, tile in enumerate(row):
                # if number in game map represents goo
                if tile == "4":
                    # add a 16x8 rect to the list
                    self._goo_pools.append(
                        pygame.Rect(x * self.CHUNK_SIZE, y * self.CHUNK_SIZE
                                    + self.CHUNK_SIZE / 2, self.CHUNK_SIZE,
                                    self.CHUNK_SIZE / 2))

    def get_goo_pools(self):
        """
        Return list containing goo pool rects
        """
        return self._goo_pools

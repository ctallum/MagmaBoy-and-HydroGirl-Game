import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        pass

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
        self.game_map = []

        with open(path) as f:
            for line in f:
                line = line.strip().split(',')  # convert string to list of str
                self.game_map.append(line)

    def load_images(self):
        """
        Load all board chunk textures from local folder "data/board_textures

        Save textures in a dictionary.
        """
        self.board_image = {
            "wall": pygame.image.load('data/board_textures/wall.png'),
            "floor_100": pygame.image.load('data/board_textures/100.png'),
            "floor_100": pygame.image.load('data/board_textures/100.png'),
            "floor_111": pygame.image.load('data/board_textures/111.png'),
            "floor_112": pygame.image.load('data/board_textures/112.png'),
            "floor_113": pygame.image.load('data/board_textures/113.png'),
            "floor_114": pygame.image.load('data/board_textures/114.png'),
            "floor_121": pygame.image.load('data/board_textures/121.png'),
            "floor_122": pygame.image.load('data/board_textures/122.png'),
            "floor_123": pygame.image.load('data/board_textures/123.png'),
            "floor_124": pygame.image.load('data/board_textures/124.png'),
            "lava_image": pygame.image.load('data/board_textures/lava.png'),
            "water_image": pygame.image.load('data/board_textures/puddle.png'),
            "goo_image": pygame.image.load('data/board_textures/goo.png')
        }
        for texture in self.board_image.keys():
            self.board_image[texture].set_colorkey((255, 0, 255))


    def make_solid_blocks(self):
        """
        Iterate through the map and make the walls and ground solid blocks
        which the player can collide with.
        """
        self.solid_blocks = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile not in ['0', '2', '3', '4']:
                    self.solid_blocks.append(
                        pygame.Rect(x * 16, y * 16, 16, 16))

    def get_solid_blocks(self):
        """
        Return a list of pygame rects that are solid.
        """
        return self.solid_blocks

    def make_lava_pools(self):
        self.lava_pools = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == "2":
                    self.lava_pools.append(
                        pygame.Rect(x * 16, y * 16 + 8, 16, 8))
        
    def get_lava_pools(self):
        return self.lava_pools

    def make_water_pools(self):
        self.water_pools = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == "3":
                    self.water_pools.append(
                        pygame.Rect(x * 16, y * 16 + 8, 16, 8))

    def get_water_pools(self):
        return self.water_pools

    def make_goo_pools(self):
        self.goo_pools = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == "4":
                    self.goo_pools.append(
                        pygame.Rect(x * 16, y * 16 + 8, 16, 8))

    def get_goo_pools(self):
        return self.goo_pools


class Level_1(Board):
    def __init__(self):
        level = "data/level0.txt"  # we can change level design by changing txt file
        self.load_map(level)
        self.load_images()
        self.make_solid_blocks()
        self.make_water_pools()
        self.make_lava_pools()
        self.make_goo_pools()

class Level_2(Board):
    pass
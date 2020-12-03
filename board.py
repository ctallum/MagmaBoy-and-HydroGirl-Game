import sys
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        """
        Initialize pygame window and internal display.

        The internal display is a smaller resolution than the window display.
        The internal display is scaled up to match the larger window display.
        """
        # create pygame window
        SCALE = 20
        WINDOW_SIZE = (32 * SCALE, 24 * SCALE)  # final window size
        self.screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        pygame.display.set_caption("Magma Boy and Hydro Girl")

        # create internal game display
        CHUNK_SIZE = 16
        DISPLAY_SIZE = (32 * CHUNK_SIZE, 24 * CHUNK_SIZE)
        self.display = pygame.Surface(DISPLAY_SIZE)

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
            "wall": pygame.image.load('data/board_textures/0.png'),
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
            "lava_image": pygame.image.load('data/board_textures/2.png'),
            "water_image": pygame.image.load('data/board_textures/3.png'),
            "goo_image": pygame.image.load('data/board_textures/4.png')
        }

    def draw_board(self):
        """
        Draw the board.

        Iterate through the game map draw each chunk.
        """
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile == '0':
                    self.display.blit(self.board_image["wall"], (x*16, y*16))
                if tile == '100':
                    self.display.blit(self.board_image["floor_100"], (x*16, y*16))
                if tile == '111':
                    self.display.blit(self.board_image["floor_111"], (x*16, y*16))
                if tile == '112':
                    self.display.blit(self.board_image["floor_112"], (x*16, y*16))
                if tile == '113':
                    self.display.blit(self.board_image["floor_113"], (x*16, y*16))
                if tile == '114':
                    self.display.blit(self.board_image["floor_114"], (x*16, y*16))
                if tile == '121':
                    self.display.blit(self.board_image["floor_121"], (x*16, y*16))
                if tile == '122':
                    self.display.blit(self.board_image["floor_122"], (x*16, y*16))
                if tile == '123':
                    self.display.blit(self.board_image["floor_123"], (x*16, y*16))
                if tile == '124':
                    self.display.blit(self.board_image["floor_124"], (x*16, y*16))
                if tile == '2':
                    self.display.blit(self.board_image["lava_image"], (x*16, y*16))
                if tile == '3':
                    self.display.blit(self.board_image["water_image"], (x*16, y*16))
                if tile == '4':
                    self.display.blit(self.board_image["goo_image"], (x*16, y*16))
        
    def make_solid_blocks(self):
        """
        Iterate through the map and make the walls and ground solid blocks
        which the player can collide with.
        """
        self.solid_blocks = []
        for y, row in enumerate(self.game_map):
            for x, tile in enumerate(row):
                if tile not in ['0', '2', '3', '4']:
                    self.solid_blocks.append(pygame.Rect(x*16, y*16, 16, 16))

    def get_solid_blocks(self):
        """
        Return a list of pygame rects that are solid.
        """
        return self.solid_blocks

    def refresh(self):
        """
        refresh the game screen
        """
        new_window_size, center_cords = self.adjust_scale()
        game_disp = pygame.transform.scale(self.display, new_window_size)
        self.screen.blit(game_disp, center_cords)
        pygame.display.update()

    def adjust_scale(self):
        """
        Adjust internal screen for window scaling

        If the window size is changed, scale the game to the maximum amount
        while keeping the same aspect ratio. Also keep the game centered in the
        window.

        Returns:
            display_size::tuple (height, width)
                The updated height and width of the internal game display
            cords::tuple (x_cord, y_cord)
                The cordinates of the upper left corner of the internal game
                display so that when it is blit onto window, it is centered.
        """
        window_size = self.screen.get_size()

        if window_size[0]/window_size[1]>= 1.5:
            display_size = (int(1.5 * window_size[1]), window_size[1])
        else:
            display_size = (window_size[0], int(.75 * window_size[0]))
        cords = ((window_size[0] - display_size[0])/2, (window_size[1] - display_size[1])/2)

        return display_size, cords

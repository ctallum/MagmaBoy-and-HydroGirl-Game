import sys
import pygame
from pygame.locals import *

class Gates:
    def __init__(self):
        self.gate_image = pygame.image.load('data/gates_and_plates/gate.png')
        self.plate_image = pygame.image.load('data/gates_and_plates/plate.png')
        self.pplate_1 = (8,10)
        self.pplate_2 = (22,10)
        self.gate = pygame.Rect(16, 350, self.gate_image.get_width(), self.gate_image.get_height())
        self.pplate_is_pressed = False
        self.gate_is_open = False

    #def if press open or close
        #animate or disappear

    def get_moving_blocks(self):
        self.moving_block_loc = []
        return self.moving_block_loc.append(self.gate)

    def get_pplate_loc(self):
            self.moving_pplate_loc = []
            self.moving_pplate_loc.append(self.pplate_1)
            self.moving_pplate_loc.append(self.pplate_2)
            return self.moving_pplate_loc

    #def load_images(self):
        #load pics
